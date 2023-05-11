"""

    """

from pathlib import Path

import pandas as pd
from githubdata import GitHubDataRepo
from mirutil.jdate import convert_jdate_to_date_from_str
from persiantools.jdatetime import JalaliDateTime

import ns
from main import FPN
from main import Params

gdu = ns.GDU()
c = ns.Col()

pa = Params()
fpn = FPN()

def main() :
    pass

    ##
    # get latest target data ids
    gtr = GitHubDataRepo(gdu.trg)

    ##
    gtr.clone_overwrite()

    ##
    df = gtr.read_data()

    ##
    # drop date column, later will be added again
    df = df.drop(columns = [c.d])

    ##
    # read new data from temp save
    dfn = pd.read_parquet(fpn.new_data)

    ##
    # rename new data column
    new_col = c.tedpix_close + '-new'
    ren_col = {
            c.tedpix_close : new_col
            }

    dfn = dfn.rename(columns = ren_col)

    ##
    # merge old & new data
    df = df.merge(dfn , how = 'outer')

    ##
    # replace new data to old
    msk = df[new_col].notna()
    df.loc[msk , c.tedpix_close] = df[new_col]

    ##
    # drop new col
    df = df.drop(columns = new_col)

    ##
    # check no duplicated days
    assert df[c.jd].is_unique

    ##
    # make date column again
    fu = lambda x : convert_jdate_to_date_from_str(x , sep = '-')
    df[c.d] = df[c.jd].apply(fu)

    ##
    # reorder cols for beauty
    df = df[[c.d , c.jd , c.tedpix_close]]

    ##
    # convert all data to string
    df = df.astype('string')

    ##
    # save final data
    df.to_parquet(gtr.data_fp , index = False)

    ##
    tjd = JalaliDateTime.now().strftime('%Y-%m-%d')

    ##
    msg = 'Updated on ' + tjd
    msg += ' by ' + gdu.slf

    ##
    # upload data
    gtr.commit_and_push(msg , branch = 'main')

    ##
    gtr.rmdir()

    ##
    fpn.new_data.unlink()

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
