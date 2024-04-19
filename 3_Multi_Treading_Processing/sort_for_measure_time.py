"""
Відсортувати файли в папці.
"""

import time
import argparse
from pathlib import Path
from shutil import move, rmtree
from threading import Thread
import logging


def grabs_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            grabs_folder(el)


def move_file(path: Path) -> None:
    for el in path.iterdir():
        if el.is_file():
            ext = el.suffix[1:]
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                move(el, ext_folder / el.name)
            except OSError as err:
                logging.error(err)


if __name__ == "__main__":

    """
    --source [-s] 
    --output [-o] default folder = dist
    """

    parser = argparse.ArgumentParser(description="Sorting folder")
    parser.add_argument("--source", "-s", help="Source folder. ATTENTION - will be deleted", required=True)
    parser.add_argument("--output", "-o", help="Output folder", default="dist")

    args = vars(parser.parse_args())
    print("Data fo sort files:", args)

    source = Path(args.get("source"))
    output = Path(args.get("output"))

    folders = []
    folders.append(source)
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")


    # start_time = time.time()
    # grabs_folder(source)
    # grab_time = time.time() - start_time
    # print("grab folders:", folders)


    start_time = time.time()
    grab_threads = []
    for el in source.iterdir():
        if el.is_dir():
            folders.append(el)
            grab_th = Thread(target=grabs_folder, args=(el,))
            grab_th.start()
            grab_threads.append(grab_th)

    [grab_th.join() for grab_th in grab_threads]

    th_time = time.time() - start_time
    print("threads folders:", folders)

    print("simple_grab", th_time)
    print("threads_grab", th_time)


    # start_time = time.time()
    # rm_threads = []
    # for folder in folders:
    #     move_file(folder)

    # move_time = time.time() - start_time
    # rmtree(source)


    start_time = time.time()
    rm_threads = []
    for folder in folders:
        rm_th = Thread(target=move_file, args=(folder,))
        rm_th.start()
        rm_threads.append(rm_th)

    [rm_th.join() for rm_th in rm_threads]

    move_time = time.time() - start_time
    rmtree(source)
    

    print(f"Folder {source} sorted and deleted. Find your files in folder {output}")
    print("Time for move files to folders:", move_time)