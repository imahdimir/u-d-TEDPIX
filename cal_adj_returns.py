"""

    """

from pathlib import Path

import pandas as pd
from githubdata import GitHubDataRepo
from mirutil.ns import update_ns_module
from persiantools.jdatetime import JalaliDateTime

update_ns_module()
import ns

gdu = ns.GDU()
c = ns.Col()

sfp = Path('temp.prq')

class Const :
    ind_url = 'http://www.tsetmc.com/tsev2/chart/data/Index.aspx?i={}&t=value'
    headers = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }

cte = Const()

class ColName :
    pass

cn = ColName()

def make_index_url(id) :
    return cte.ind_url.format(id , 1)

def main() :
    pass

    ##

    ##

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
