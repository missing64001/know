function run_ajax(ldata) {
    $.ajax({
        url:"/getdata/",
        data:ldata,
        type:"get",
        datatype:"json",
        success:function(data){

            if (ldata['search'])
            {
                data = JSON.parse(data);
                var tree = $('#tree')
                tree.html("")

                for (var i = 0; i < data.length; i++) {
                    var da = data[i]
                    var name = da[0]
                    var cid = da[1]
                    var ctype = da[2]
                    var explan = da[3]
                    var children = da[4]
                    var ul = $("<ul></ul>")
                    var li = $("<li></li>")
                    var span
                    if (ctype == 'l'){
                        span = $("<span class='folder'></sapn>")
                    }
                    else if (ctype == 'c'){
                        span = $("<span class='file' onclick='itemclick(this)'></sapn>")
                    }
                    li.append(span)
                    li.append(ul)
                    tree.append(li)

                    span.text(name)
                    span.attr('cid',cid)
                    span.attr('ctype',ctype)
                    span.attr('explan',explan)
                    if (children){
                        set_chlidre(ul,children)
                    }

                }
                tree.treeview();
            }
            else if(ldata['ctype'] == 'c'){
                // console.log('finish')
                $('textarea').text(data)

            }
            else{
                // console.log('nofinish')
                // console.log(ldata)
            }
            


        },
        error:function(err){
            alert('err:'+err)
            // document.write('run_ajax 出错了')
        }
    })
}

function set_chlidre(pul,pchildren) {
    // console.log(pchildren)
    for (var i = 0; i < pchildren.length; i++) {
        var da = pchildren[i]
        var name = da[0]
        var cid = da[1]
        var ctype = da[2]
        var explan = da[3]
        var children = da[4]

        // console.log(cid,ctype,explan,children)
        var ul = $("<ul></ul>")
        var li = $("<li></li>")
        var span
        if (ctype == 'l'){
            span = $("<span class='folder'></sapn>")
        }
        else if (ctype == 'c'){
            span = $("<span class='file' onclick='itemclick(this)'></sapn>")
        }
        li.append(span)
        li.append(ul)
        pul.append(li)

        span.text(name)
        span.attr('cid',cid)
        span.attr('ctype',ctype)
        span.attr('explan',explan)

        if (children){
            set_chlidre(ul,children)
        }
    }
}

// $(function(){
//     run_ajax({"id":33,"type":"c"})
//     runtree()
// });


function input_change(tt) {
    run_ajax({"search":$(tt).val()})
    runtree()
}


function itemclick(tt) {
    cid = $(tt).attr('cid')
    ctype = $(tt).attr('ctype')
    run_ajax({"cid":cid,"ctype":ctype})
}