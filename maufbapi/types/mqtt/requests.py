# mautrix-facebook - A Matrix-Facebook Messenger puppeting bridge.
# Copyright (C) 2021 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from typing import Dict

from attr import dataclass

from maufbapi.thrift import TType, ThriftObject, field, autospec


@autospec
@dataclass(kw_only=True)
class SendMessageRequest(ThriftObject):
    # tfbid_<groupid> for groups, plain user id for users
    chat_id: str
    message: str
    offline_threading_id: int = field(TType.I64)
    # index 4: ???
    # Example values:
    #   'is_in_chatheads': 'false'
    #   'ld': '{"u":1674434.........}'
    #   'entrypoint': 'messenger_inbox:in_thread'
    #   'trigger': '2:thread_list:thread' or 'thread_view_messages_fragment_unknown'
    #   'active_now': '{"is_online":"false","last_active_seconds":"1431"}'
    flags: Dict[str, str] = field(index=5, factory=lambda: {})
    # 369239263222822 = "like"
    sticker: str = field(default=None)
    # indices 7-11: ???
    sender_id: int = field(TType.I64, index=12)
    # indices 13-17: ???
    unknown_int32: int = field(TType.I32, index=18, default=0)
    # index 19: ???
    extra_metadata: Dict[str, str] = field(index=20, default=None)
    unknown_int64: int = field(TType.I64, index=21, default=0)
    # index 22: ???
    unknown_bool: bool = field(TType.BOOL, index=23, default=False)
    # this is weird int64 that looks like offline_threading_id, but isn't quite the same
    tid2: int = field(TType.I64, index=24)
