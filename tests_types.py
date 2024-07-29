### This program for testing different types of data в Python
import time

amount_operations = 100000000
lst, st, dct = [], set(), {}

def create(type_dt):
    if type_dt == "list":
        for i in range(amount_operations): lst.append(i)

    if type_dt == "tpl":
        global tpl
        tpl = tuple(range(amount_operations))

    if type_dt == "set":
        for i in range(amount_operations): st.add(i)

    if type_dt == "dct":
        for i in range(amount_operations): dct[i] = i


def find_el(type_dt):
    if type_dt == "list":
        if amount_operations - 1 in lst: pass

    if type_dt == "tpl":
        if amount_operations - 1 in tpl: pass

    if type_dt == "set":
        if amount_operations - 1 in st: pass

    if type_dt == "dct":
        if amount_operations - 1 in dct: pass


def remove_el(type_dt):
    if type_dt == "list":
        for i in range(amount_operations):  lst.pop()

    if type_dt == "set":
        for i in range(amount_operations): st.remove(i)

    if type_dt == "dct":
        for i in range(amount_operations): del dct[i]


def timers(operation):
    start_time = time.time()
    if operation == "create_list": create("list")
    if operation == "find_el_in_lst": find_el("list")
    if operation == "remove_el_from_lst": remove_el("list")

    if operation == "create_tpl": create("tpl")
    if operation == "find_el_in_tpl": find_el("tpl")

    if operation == "create_set": create("set")
    if operation == "find_el_in_set": find_el("set")
    if operation == "remove_el_from_set": remove_el("set")

    if operation == "create_dct": create("dct")
    if operation == "find_el_in_dct": find_el("dct")
    if operation == "remove_el_from_dct": remove_el("dct")
    end_time = time.time()

    if operation == "create_list": print(f"{amount_operations} elements were"
                                         f" added to the list in {round(end_time - start_time, 4)} sec.")
    if operation == "find_el_in_lst": print(f"Finding the element took only {round(end_time - start_time, 4)} sec.")
    if operation == "remove_el_from_lst": print(f"Removal of {amount_operations} elements from the"
                                                f" list occurred in {round(end_time - start_time, 4)} sec.")

    if operation == "create_tpl": print(f"Creating a tuple with {amount_operations} elements "
                                        f"took {end_time - start_time:.4f} sec.")

    if operation == "find_el_in_tpl": print(f"Finding the element took only {round(end_time - start_time, 4)} sec.")

    if operation == "create_set": print(f"The set was updated with {amount_operations} elements "
                                        f"in {round(end_time - start_time, 4)} sec.")
    if operation == "find_el_in_set": print(f"Finding the element took only {round(end_time - start_time, 4)} sec.")
    if operation == "remove_el_from_set": print(f"The removal of elements from the set {amount_operations} occurred "
                                                f"in {round(end_time - start_time, 4)} sec.")
    if operation == "create_dct": print(f"{amount_operations} key-value pairs were "
                                        f"added to the dictionary in {round(end_time - start_time, 4)} sec.")
    if operation == "find_el_in_dct": print(f"The key search took only {round(end_time - start_time, 4)} sec.")
    if operation == "remove_el_from_dct": print(f"{amount_operations} key-value pairs were removed from "
                                                f"the dictionary in {round(end_time - start_time, 4)} sec.")


def test_all_types(type_data):
    if type_data == "list":
        timers("create_list")
        timers("find_el_in_lst")
        timers("remove_el_from_lst")
    if type_data == "tpl":
        timers("create_tpl")
        timers("find_el_in_tpl")
    if type_data == "set":
        timers("create_set")
        timers("find_el_in_set")
        timers("remove_el_from_set")
    if type_data == "dct":
        timers("create_dct")
        timers("find_el_in_dct")
        timers("remove_el_from_dct")

if __name__ == "__main__":
    test_all_types("list")
    test_all_types("tpl")
    test_all_types("set")
    test_all_types("dct")