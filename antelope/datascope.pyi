class Dbptr(object):
    def __init__(self, copy=None):
        ...

    def add(self, record=None): ...
    def addnull(self) : ...
    def addv(self, *args, table=None): ...
    def close(self) : ...
    def crunch(self) : ...
    def delete(self) : ...
    def destroy(self) : ...
    def ex_eval(self, expr, type=0): ...
    def extfile(self, tablename=None): ...
    def filename(self) : ...
    def find(self, expr, first=-1, reverse=False) -> 'Dbptr': ...
    def find_join_keys(self, dbt): ...
    def find_join_tables(self) : ...
    def free(self) : ...
    def get(self, scratch=False): ...
    def get_range(self, bundlefield='bundle'): ...
    def getv(self, *args, table=None): ...
    def group(self, groupfields, name=None, type=1): ...
    def iter_record(self, start, stop, step=None): ...
    def list2subset(self, list=None): ...
    def lookup(self, database=None, table=None, field=None, record=None) -> 'Dbptr': return Dbptr()
    def map_seed_chanloc(self, sta, schan, sloc): ...
    def map_seed_netsta(self, snet, ssta): ...
    def mark(self) : ...
    def matches(self, dbt, kpattern=None, tpattern=None): ...
    def nextid(self, name): ...
    def process(self, list): ...
    def put(self, record=None): ...
    def putv(self, *args, table=None): ...
    def query(self, dbcode): ...
    def save_view(self) : ...
    def seed_loc(self, sta, chan): ...
    def seed_net(self, sta): ...
    def separate(self, tablename): ...
    def sever(self, tablename, name=None): ...
    def sort(self, keys, unique=False, reverse=False, name=None): ...
    def subset(self, expr, name=None): ...
    def theta(self, db2in, ex_str, outer=False, name=None): ...
    def to_pipe(self, fileobj, records=None): ...
    def trapply_calib(self) : ...
    def trcopy(self, trout=None): ...
    def trdata(self) : ...
    def trdatabins(self, binsize): ...
    def trdestroy(self) : ...
    def trfilter(self, filter_string): ...
    def trfree(self) : ...
    def trload_css(self, t0, t1, tr=None, table=None): ...
    def trload_cssgrp(self, t0, t1, tr=None, table=None): ...
    def trloadchan(self, t0, t1, sta, chan): ...
    def trputdata(self, data): ...
    def trrotate(self, phi_deg, theta_deg, newchan): ...
    def trrotate_to_standard(self, newchan=('E', 'N', 'Z')): ...
    def trsample(self, t0, t1, sta, chan, apply_calib=False, filter=None): ...
    def trsplice(self) : ...
    def trsplit(self) : ...
    def trtruncate(self, leave): ...
    def truncate(self, nrecords): ...
    def trwfname(self, pattern=None): ...
    def ungroup(self, name=None): ...
    def unjoin(self, database_name, rewrite=False): ...
    def write_view(self, fileobj): ...


def dbopen(path) -> Dbptr:
    return Dbptr()
