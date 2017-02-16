# -*- coding:utf-8 -*-

import unittest

from studio.lp_dataocean_handle.lp_jiuyao_multi_loan_denied_count import Handle

data = {
    'loanInfos': [
        {
            'borrowType': 1,
            'borrowState': 2,
            'borrowAmount': 3,
            'contractDate': 1343779200000,
            'loanPeriod': 24,
            'repayState': 7,
            'arrearsAmount': 0,
            'companyCode': 'P2P4HJK0000100010'
        },
        {
            'borrowType': 1,
            'borrowState': 1,
            'borrowAmount': 3,
            'contractDate': 1343779200000,
            'loanPeriod': 24,
            'repayState': 7,
            'arrearsAmount': 0,
            'companyCode': 'P2P4HJK0000100011'
        },
        {
            'borrowType': 1,
            'borrowState': 1,
            'borrowAmount': 3,
            'contractDate': 1343779200000,
            'loanPeriod': 24,
            'repayState': 7,
            'arrearsAmount': 0,
            'companyCode': 'P2P4HJK0000100011'
        }
    ]
}


class TestPlugin(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_lp_jiuyao_multi_loan_denied_count(self):
        handler = Handle(self.data)
        res = handler.handle()
        print res


if __name__ == '__main__':
    unittest.main()
