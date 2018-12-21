## for django
import sys
import os

from pprint import pprint
# import sip
from hmysql import models,Q,timezone
import time
from django.db import connection
from functools import reduce
import re
import traceback
import pyperclip
import datetime
import pickle
from func.hcalendar import HCalendar


class getdata(object):
    def __init__(self):
        self.get_labels_by_content = {}
        self.get_contents_by_label = {}
        self.labeldict = {}
        self.contentdict = {}


    def set_all_data(self):


        def set_content_labels():
            cursor = connection.cursor()
            sql = 'select content_id,label_id from data_content_labels;'
            cursor.execute(sql)
            rows = cursor.fetchall()

            for row in rows:
                labels_set = self.get_labels_by_content.get(row[0])
                if not labels_set:
                    self.get_labels_by_content[row[0]] = {row[1]}
                else:
                    labels_set.add(row[1])

                contents_set = self.get_contents_by_label.get(row[1])
                if not contents_set:
                    self.get_contents_by_label[row[1]] = {row[0]}
                else:
                    contents_set.add(row[0])

        labelall = models.Label.objects.all()
        contentall = models.Content.objects.all()
        

        for label in labelall:
            self.labeldict[label.id] = label
        

        for content in contentall:
            self.contentdict[content.id] = content

        
        set_content_labels()

    def get_contents_by_textlst(self,textlst):
        # return content_id_set_by_text,label_id_set
        def get_label_children(label_id_set):
            llen = len(label_id_set)
            for i in self.labeldict:
                label = self.labeldict[i]
                if label.pid in label_id_set:
                    label_id_set.add(label.id)
            if llen != len(label_id_set):
                get_label_children(label_id_set)

        content_id_set_by_label_lst = []
        content_id_set_by_text_lst = []
        content_id_set_by_true_text_lst = []
        label_id_set_lst = []
        for text in textlst:
            # content_id_set_by_label = set()
            content_id_set_by_text = set()
            # content_id_set_by_true_text = set()
            label_id_set = set()
            for i in self.labeldict:
                label = self.labeldict[i]
                if text in label.name:
                    label_id_set.add(label.id)


            get_label_children(label_id_set)

            # pprint(label_id_set)

            # for id_ in label_id_set:
            #     content_id_set_by_label |= self.get_contents_by_label.get(id_,set())

            for id_,content in self.contentdict.items():
                if text in content.name:
                    content_id_set_by_text.add(id_)
                elif text in content.text:
                    content_id_set_by_text.add(id_)



            # content_id_set_by_label_lst.append(content_id_set_by_label)
            content_id_set_by_text_lst.append(content_id_set_by_text)
            # content_id_set_by_true_text_lst.append(content_id_set_by_true_text)
            label_id_set_lst.append(label_id_set)



        content_id_set_by_text = reduce(lambda x,y:x & y,content_id_set_by_text_lst)
        # content_id_set_by_label = reduce(lambda x,y:x & y,content_id_set_by_label_lst)
        # content_id_set_by_true_text = reduce(lambda x,y:x & y,content_id_set_by_true_text_lst)
        label_id_set = reduce(lambda x,y:x & y,label_id_set_lst)

        # print(content_id_set_by_label)
        # print('是不是可以把 content_id_set_by_label 删除')
        
        return content_id_set_by_text,label_id_set

    def set_label_treeitems(self,label_id_set):
        labels = [self.labeldict[i] for i in label_id_set]
        labels_values = [{
                            'id':self.labeldict[i].id,
                            'name':self.labeldict[i].name,
                            'pid':self.labeldict[i].pid,
                            'queue':self.labeldict[i].queue,
                            'grade':self.labeldict[i].grade,
                            'create_date':self.labeldict[i].create_date,
                        } 
                        for i in label_id_set]

        queue_queue = {'data':None,'children':{}}
        queue_child_dict = {1:queue_queue['children']}
        rest = {}
        for i in range(len(labels)):
            la = labels[i]
            labels_values[i]['object'] = la




            id = labels_values[i]['id']
            name = labels_values[i]['name']
            pid = labels_values[i]['pid']
            queue = labels_values[i]['queue']
            grade = labels_values[i]['grade']
            create_date = labels_values[i]['create_date']

            if pid == -1:
                queue_queue['data'] = labels_values[i]
            elif pid == 1:
                queue_queue['children'][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = queue_queue['children'][id]['children']
            elif pid in queue_child_dict:
                queue_child_dict[pid][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = queue_child_dict[pid][id]['children']
            elif pid in rest:
                rest[pid]['children'][id] = {'data':labels_values[i],'children':{}}
                queue_child_dict[id] = rest[pid]['children'][id]['children']
            else:
                rest[id] = {'data':labels_values[i],'children':{}}


        while rest:
            for re in rest.copy():
                id = rest[re]['data']['id']
                name = rest[re]['data']['name']
                pid = rest[re]['data']['pid']
                queue = rest[re]['data']['queue']
                grade = rest[re]['data']['grade']
                create_date = rest[re]['data']['create_date']

                if pid in queue_child_dict:
                    rest_re = rest.pop(re)
                    queue_child_dict[pid][id] = rest_re
                    queue_child_dict[id] = queue_child_dict[pid][id]['children']
                    
                elif pid in rest:
                    rest_re = rest.pop(re)
                    rest[pid]['children'][id] = rest_re
                    queue_child_dict[id] = rest[pid]['children'][id]['children']

                else:

                    rest_re = rest.pop(re)
                    queue_queue['children'][id] = rest_re
                    queue_child_dict[id] = rest_re['children']
        # pprint(queue_queue)



        def add_tree_child_item(children,labell):
            for child in children['children'].values():


                cobj = child['data']['object']
                _id = cobj.id
                name = cobj.name
                queue = cobj.queue
                create_date = cobj.create_date + datetime.timedelta(hours=8)
                create_date = create_date.strftime('%Y-%m-%d %H:%M:%S')
                _type = 'l'

                labell.append([name,_id,_type,create_date,[]])
                add_tree_child_item(child,labell[-1][-1])
            # hsort(labell,pqueue)

        labellst = []
        for fchild in queue_queue['children'].values():
            fcobj = fchild['data']['object']
            _id = fcobj.id
            name = fcobj.name
            queue = fcobj.queue
            create_date = fcobj.create_date + datetime.timedelta(hours=8)
            create_date = create_date.strftime('%Y-%m-%d %H:%M:%S')
            _type = 'l'

            labellst.append([name,_id,_type,create_date,[]])
            add_tree_child_item(fchild,labellst[-1][-1])

        return labellst
    
    def set_contents(self,labellsts,content_id_set_by_text):

        def hsort(lst,queue):
            def _hsort(x):
                try:
                    if x[2] == 'l':
                        return -label_queue_dict.get(x[1],1)
                    elif x[2] == 'c':
                        return content_queue_dict.get(x[1],len(content_queue)+10)
                except Exception:
                    print(x)
                    return 0

            label_queue_dict = {}
            content_queue_dict = {}
            label_queue = []
            content_queue = []
            if queue:
                if queue.split('|')[0]:
                    label_queue = queue.split('|')[0].split(',')
                    for i,j in enumerate(label_queue[::-1],2):
                        label_queue_dict[int(j)] = i
                if queue.split('|')[1]:
                    content_queue = queue.split('|')[1].split(',')
                    for i,j in enumerate(content_queue):
                        content_queue_dict[int(j)] = i

            lst.sort(key=_hsort)


        def add_child_content(lst,pcontent_id_set):
            for l in lst:
                lid = l[1]
                lobj = self.labeldict[lid]
                queue = lobj.queue
                content_id_set = self.get_contents_by_label.get(lid,[])

                add_child_content(l[4],content_id_set)
                # print(l[4])
                hsort(l[4],queue)

            for i in pcontent_id_set:
                cobj = self.contentdict[i]

                _id = cobj.id
                name = cobj.name
                create_date = cobj.create_date + datetime.timedelta(hours=8)
                create_date = create_date.strftime('%Y-%m-%d %H:%M:%S')
                _type = 'c'
                lst.append([name,_id,_type,create_date])


        for labellst in labellsts:
            lid = labellst[1]
            lobj = self.labeldict[lid]
            queue = lobj.queue


            content_id_set = self.get_contents_by_label.get(lid,[])

            add_child_content(labellst[4],content_id_set)
            # print(l[4])
            hsort(labellst[4],queue)


        for i in content_id_set_by_text:
            cobj = self.contentdict[i]

            _id = cobj.id
            name = cobj.name
            create_date = cobj.create_date + datetime.timedelta(hours=8)
            create_date = create_date.strftime('%Y-%m-%d %H:%M:%S')
            _type = 'c'
            labellsts.append([name,_id,_type,create_date])
