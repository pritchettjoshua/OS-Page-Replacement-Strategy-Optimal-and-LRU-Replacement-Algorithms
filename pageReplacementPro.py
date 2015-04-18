__author__ = 'joshua pritchett'
import random

# define reference length
reference_length = 5000
#define optimal page replacement
def optimal_replacement(ref, resident_set_limit):
    page_faults = 0
    resident = []
    counter = 0
    OUTFILE = open("Opt_residentList.csv", 'w')
    for page in ref:
        OUTFILE.write(str(resident)+"\n")
        if page not in resident:
            if len(resident) < resident_set_limit:
                #append because the resident size limit hasn't been maxed
                resident.append(page)
                page_faults += 1
            else:
                # resident size is maxed, so we need to remove a page
                # find the page we are going to use last, remove it
                list_of_pages = list(resident)
                # eliminate from list of pages until one is left, then remove that page from resident set
                for todo in ref[counter:]:
                    if len(list_of_pages) == 1:
                        # we have found the page used the furthest in the future
                        # remove it
                        # add the new page, increment page fault.
                        break
                    if todo in list_of_pages:
                        list_of_pages.remove(todo)
                resident.remove(list_of_pages[0])
                resident.append(page)
                page_faults += 1
        counter += 1
    OUTFILE.close
    return page_faults


def least_recently_used_replacement(ref, resident_set_limit):
    page_faults = 0
    resident = []
    counter = 0
    OUTFILE = open("LRU_residentList.csv", 'w')
    for page in ref:
        OUTFILE.write(str(resident)+"\n")
        if page not in resident:
            if len(resident) < resident_set_limit:
                # append page because resident size limit not maxed
                resident.append(page)
                page_faults += 1
            else:
                # need to remove a page
                list_of_pages = list(resident)
                # remove from list of pages until one is left
                for todo in reversed(ref[:counter + 1]):
                    if len(list_of_pages) == 1:
                        # we have found the page used the furthest in the future
                        # remove it
                        # add the new page, increment page fault.
                        break
                    if todo in list_of_pages:
                        list_of_pages.remove(todo)
                resident.remove(list_of_pages[0])
                resident.append(page)
                page_faults += 1
        counter += 1
    OUTFILE.close
    return page_faults

def ninety_ten_rule():
    results = []
    for num in range(0, reference_length):
        if random.random() < 0.9:
            results.append(int(random.random() * 10))
        else:
            results.append(int(random.random() * 90) + 10)
    OUTFILE = open("pages.csv", 'w')
    OUTFILE.write(str(results))
    OUTFILE.close
    return results

# main method
print("The page replacement program has started, please wait for results")
OUTFILE = open("pageReplacementProOutput5000.csv", 'w')
OUTFILE.write("resident_length, resident_size, optimal_replacement, least_recently_used_replacement \n")
referenceList = ninety_ten_rule()
for resident_size in range(1, 100):
    optimal_replacement_var = optimal_replacement(referenceList, resident_size)
    least_recently_used_replacement_var = least_recently_used_replacement(referenceList, resident_size)
    line = str(reference_length) + ", " + str(resident_size) + ", " + str(optimal_replacement_var) + ", " + str(least_recently_used_replacement_var) + "\n"
    OUTFILE.write(line)
OUTFILE.close
print("The page replacement program has ended, please check pageReplacementProOutput5000.csv for results")