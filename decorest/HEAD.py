# -*- coding: utf-8 -*-
#
# Copyright 2018 Bartosz Kryza <bkryza@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""HEAD Http method decorator."""

from functools import wraps

from .client import HttpMethod
from .decorators import HttpMethodDecorator, set_decor


class HEAD(HttpMethodDecorator):
    """HEAD HTTP method decorator."""

    def __init__(self, path):
        """Initialize with endpoint relative path."""
        super(HEAD, self).__init__(path)

    def __call__(self, func):
        """Callable operator."""
        set_decor(func, 'http_method', HttpMethod.HEAD)

        @wraps(func)
        def options_decorator(*args, **kwargs):
            return super(HEAD, self).call(func, *args, **kwargs)

        return options_decorator
