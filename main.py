"""

    """

from pathlib import Path

from mirutil.ns import rm_ns_module
from mirutil.ns import update_ns_module

update_ns_module()
import ns

_ = ns.GDU()

class FPN :
    new_data = Path('temp-new.prq')

class Params :
    ind_url = 'http://www.tsetmc.com/tsev2/chart/data/Index.aspx?i={}&t=value'
    headers = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
            }

    tedpix_id = 'TEDPIX'
    tedpix_tsetmc_id = None

def main() :
    pass

    ##

    import get_new_data
    import check_upload_data

    ##
    get_new_data.main()

    ##
    check_upload_data.main()

    ##
    rm_ns_module()

    ##

##


if __name__ == "__main__" :
    main()
    print(f'{Path(__file__).name} Done!')
