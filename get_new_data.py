"""

    """

import time
from pathlib import Path

import pandas as pd
import requests
from githubdata import GitHubDataRepo
from mirutil.jdate import make_zero_padded_jdate_ie_iso_fmt

import ns
from main import FPN
from main import Params

gdu = ns.GDU()
c = ns.Col()

pa = Params()
fpn = FPN()

def make_index_url(index_id) :
    return pa.ind_url.format(index_id , 1)

def make_df_from_csv_resp(r) :
    df = pd.DataFrame(r.text.split(';'))
    return df[0].str.split(',' , expand = True)

def main() :
    pass

    ##
    # get indices ids
    gsa = GitHubDataRepo(gdu.srca)

    ##
    gsa.clone_overwrite()

    ##
    df = gsa.read_data()

    ##
    # remove index ids data
    gsa.rmdir()

    ##
    # find tedpix's tsetmc id
    msk = df[c.ind_id].eq(pa.tedpix_id)
    idx = msk[msk].index[0]
    print(idx)

    ##
    pa.tedpix_id = df.at[idx , c.tse_id]
    pa.tedpix_id = str(pa.tedpix_id)
    print(pa.tedpix_id)

    ##
    # make index data url
    url = make_index_url(pa.tedpix_id)
    print(url)

    ##
    # try to get the response multiple times
    for _ in range(10) :
        r = requests.get(url , headers = pa.headers)

        if r.status_code == 200 :
            break

        time.sleep(1)

    ##
    if r.status_code != 200 :
        raise "No response from TSETMC server"

    ##
    df = make_df_from_csv_resp(r)

    ##
    # rename cols
    df.columns = [c.jd , c.tedpix_close]

    ##
    # make jdate iso format
    fu = lambda x : make_zero_padded_jdate_ie_iso_fmt(x , sep = '/')
    df[c.jd] = df[c.jd].apply(fu)

    ##
    df.to_parquet(fpn.new_data , index = False)

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
