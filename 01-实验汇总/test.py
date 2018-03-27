def add(dict_info):
    backend = dict_info.get('backend')
    record_list = fetch(backend)
    backend_title = "backend %s" % backend
    current_record = "server %s %s weight %d maxconn %d" % (dict_info['record']['server'], dict_info['record']['server'], dict_info['record']['weight'], dict_info['record']['maxconn'])
    if not record_list:
        record_list.append(backend_title)
        record_list.append(current_record)
        with open('ha') as read_file, open('ha.new', 'w') as write_file:
            flag = False
            for line in read_file:
                write_file.write(line)
            for i in record_list:
                if i.startswith('backend'):
                    write_file.write(i+'\n')
                else:
                    write_file.write("%s%s\n" % (8*" ", i))
    else:
        record_list.insert(0, backend_title)
        if current_record not in record_list:
            record_list.append(current_record)

        with open('ha') as read_file, open('ha.new', 'w') as write_file:
            flag = False
            has_write = False
            for line in read_file:
                line_strip = line.strip()
                if line_strip == backend_title:
                    flag = True
                    continue
                if flag and line_strip.startswith('backend'):
                    flag = False
                if not flag:
                    write_file.write(line)
                else:
                    if not has_write:
                        for i in record_list:
                            if i.startswith('backend'):
                                write_file.write(i+'\n')
                            else:
                                write_file.write("%s%s\n" % (8*" ", i))
                    has_write = True
    os.rename('ha','ha.bak')
    os.rename('ha.new','ha')
