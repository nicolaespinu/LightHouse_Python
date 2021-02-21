# lease = '''Dear Dot,
#            This document validates that you are beholden to a monthly payment of rent for this house.
#            Rent is to be paid by the first of every month.
#            Fill in your signature to agree to these terms.
#             -------------
#             Please Sign Here:
# '''
# signature = 'Nicolae Spinu';
# new_lease = f'{lease}{signature}';
# print(new_lease);

signature = 'Nicolae Spinu';

new_lease = f'''

Dear Dot, 

This document validates that you are beholden to a monthly payment of rent for this house.

Rent is to be paid by the first of every month.

Fill in your signature to agree to these terms.

-------------

Please Sign Here: {signature} 

'''
print(new_lease);
