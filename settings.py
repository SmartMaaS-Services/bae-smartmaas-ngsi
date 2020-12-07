# -*- coding: utf-8 -*-

# Copyright (c) 2019 Future Internet Consulting and Development Solutions S.L.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os import environ

UNITS = [{
    'name': 'Api call',
    'description': 'The final price is calculated based on the number of calls made to the API'
}]

# Keyrock
# URL
IDM_URL = 'http://localhost:3000'
# User email
IDM_USER = 'admin@test.com'
# User password
IDM_PASSWORD = '1234'
# Client ID API Access application
BAE_LP_OAUTH2_CLIENT_ID = ''
# Client Secret API Access application
BAE_LP_OAUTH2_CLIENT_SECRET = ''

# Client ID Marketplace application
BAE_MARKET_APP_CLIENT_ID = ''

# Tenant-Manager
# URL
TENANT_MANAGER_URL = 'http://tenantservice:5000'

IDM_USER = environ.get('BAE_ASSET_IDM_USER', IDM_USER)
IDM_PASSWORD = environ.get('BAE_ASSET_IDM_PASSWORD', IDM_PASSWORD)
IDM_URL = environ.get('BAE_ASSET_IDM_URL', IDM_URL)

CLIENT_ID = environ.get('BAE_LP_OAUTH2_CLIENT_ID', BAE_LP_OAUTH2_CLIENT_ID)
CLIENT_SECRET = environ.get('BAE_LP_OAUTH2_CLIENT_SECRET', BAE_LP_OAUTH2_CLIENT_SECRET)

MARKET_CLIENT_ID = environ.get('BAE_MARKET_APP_CLIENT_ID', BAE_MARKET_APP_CLIENT_ID)

TENANT_MANAGER_URL = environ.get('TENANT_MANAGER_URL', TENANT_MANAGER_URL)
