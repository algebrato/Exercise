#!/usr/bin/python3

import pyinotify as pnt
import asyncio

if __name__ == '__main__':

    wm = pnt.WatchManager()
    loop = asyncio.get_event_loop()
    notifier = pnt.AsyncioNotifier(wm, loop)
    wm.add_watch('/tmp', pnt.ALL_EVENTS)
    loop.run_forever()
