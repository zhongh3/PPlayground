import ast

debugging = True


def process_input(filename):

    file = open(filename, mode="r", encoding='UTF-8')

    data = file.readline().strip()

    start = data.find("<script>window.__INITIAL_STATE__=")
    if start != -1:
        start2 = data.find('"pages":[', start) + len('"pages":[')
        if start2 != -1:
            end = data.find("]", start2)
            cut = data[start2:end]  # cut: string

            if debugging:
                log_file = open("./data/cut.html", mode='w', encoding='UTF-8')
                log_file.write(cut)
                log_file.close()

            items = ast.literal_eval(cut)  # items: tuples
            out = []  # out: dictionaries

            for item in items:
                out.append(dict(item))

            return out

        else:
            raise Exception("Can't fine the string - \"<script>window.__INITIAL_STATE__=\"")
    else:
        raise Exception("Can't fine the string - \'\"pages\":[\'")


def get_cid_by_page_num(pages, page_num):
    for page in pages:
        if page.get("page") == page_num:
            if debugging:
                print("page = {}, cid = {}, title = {}".format(
                    page.get("page"), page.get("cid"), page.get("part")
                ))

            # both cid and title should be returned as string
            return str(page.get("cid")), page.get("part")


def get_cid_and_title(filename, page_num):
    pages = process_input(filename)
    return get_cid_by_page_num(pages, page_num)


def get_total_page_num(filename):
    x = len(process_input(filename))
    print("Total page number = {}".format(x))
    return x


def main():
    filename = "./data/webpage.html"
    page_num = 11

    get_cid_and_title(filename, page_num)
    get_total_page_num(filename)


if __name__ == "__main__":
    main()