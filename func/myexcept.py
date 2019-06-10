


class QuoteError(Exception):
    pass


def main():
    try:
        raise QuoteError('asddsgg')
    except QuoteError as e:
        print(e)

if __name__ == '__main__':
    main()