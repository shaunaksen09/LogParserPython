#!/usr/bin/python

domainErrors = {"total5xxCount": 0} #Initial counter for 5xx errors

def logParser(starttime, endtime, fpath):
    print("Between time " + str(starttime) + " and time " + str(endtime) + " in file " + fpath + ":")
    with open(fpath, 'r', buffering=100000) as file:
        for lines in file:
            split_line_list = [lines.strip() for lines in lines.split('|')]
            if (len(split_line_list) != 1):
                logtime = float(split_line_list[0])
                if (float(starttime) <= logtime < float(endtime)):
                    if (500 <= int(split_line_list[4].strip()) < 600):
                        domainErrors["total5xxCount"] += 1
                        if (split_line_list[2].strip() not in domainErrors.keys()):  # Append to existing domain or create new domain key
                            domainErrors[split_line_list[2].strip()] = 1
                        else:
                            domainErrors[split_line_list[2].strip()] += 1
    if (len(domainErrors) == 1):
        print("No 5xx errors were logged")
    else:
        for domain, count in domainErrors.items():
            if domain != "total5xxCount":
                print(str(domain) + " returned " + str((100 * count) / domainErrors["total5xxCount"]) + "% 5xx errors")  # Calculate percentage

if __name__ == '__main__':
    logParser(1493969101.644,1493969120.644,"python_log_parser/Vimeo-app.log")



