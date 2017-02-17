# Copyright (c) 2016-2017 Adobe Systems Incorporated.  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import user_sync.error
import user_sync.helper

PRODUCT_CONFIG_GROUP_TYPE = 'Product Configuration'
USER_GROUP_TYPE = 'User Group'

NORMALIZED_GROUP_TYPE_MAP = {
    user_sync.helper.normalize_string(PRODUCT_CONFIG_GROUP_TYPE): PRODUCT_CONFIG_GROUP_TYPE,
    user_sync.helper.normalize_string(USER_GROUP_TYPE): USER_GROUP_TYPE
}

def parse_group_type(value, message_format = None):
    '''
    :type value: str
    :type message_format: str
    :rtype str
    '''
    result = None
    if (value != None):
        normalized_value = user_sync.helper.normalize_string(value)
        result = NORMALIZED_GROUP_TYPE_MAP.get(normalized_value)
        if (result == None):
            validation_message = 'Unrecognized dashboard group type: "%s"' % value
            message = validation_message if message_format == None else message_format % validation_message
            raise user_sync.error.AssertionException(message)
    else:
        result = PRODUCT_CONFIG_GROUP_TYPE
    return result

