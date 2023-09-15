def modify_by_mark_image(mark_name, insert_path, insert_height=0, insert_width=0, markdown_file="README.md") -> bool:
    mark_idx_start = -1
    mark_idx_end = -1
    mark_start = "<!-- START:{} -->".format(mark_name)
    mark_end = "<!-- END:{} -->".format(mark_name)
    size = ""
    if insert_height:
        size += "height: {}px; ".format(insert_height)
    if insert_width:
        size += "width: {}px; ".format(insert_width)

    # split readme into lines
    with open(markdown_file, "r") as f:
        lines = f.readlines()

    # search for mark
    for idx, line in enumerate(lines):
        if mark_start in line:
            mark_idx_start = idx
        if mark_end in line:
            mark_idx_end = idx

    if -1 in (mark_idx_start, mark_idx_end) or (mark_idx_end <= mark_idx_start):
        return False
    
    # add image tag to markdown file
    del lines[mark_idx_start + 1: mark_idx_end]
    img_html = "<img src=\"{}\" alt=img style=\"{}\" />\n".format(insert_path, size)
    lines.insert(mark_idx_end - 1, img_html)
    with open(markdown_file, "w+") as f:
        f.write("".join(lines))
    return True


def modify_by_mark_lines(mark_name, new_lines, markdown_file="README.md") -> bool:
    mark_idx_start = -1
    mark_idx_end = -1
    mark_start = "<!-- START:{} -->".format(mark_name)
    mark_end = "<!-- END:{} -->".format(mark_name)

    # split readme into lines
    with open(markdown_file, "r") as f:
        lines = f.readlines()

    # search for mark
    for idx, line in enumerate(lines):
        if mark_start in line:
            mark_idx_start = idx
        if mark_end in line:
            mark_idx_end = idx

    if -1 in (mark_idx_start, mark_idx_end) or (mark_idx_end <= mark_idx_start):
        return False
    
    # add image tag to markdown file
    del lines[mark_idx_start + 1: mark_idx_end]
    lines[mark_idx_start + 1 : mark_idx_start + 1] = new_lines
    with open(markdown_file, "w+") as f:
        f.write("".join(lines))
    return True

    
    
    