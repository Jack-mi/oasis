# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
from dataclasses import dataclass
from typing import Any, Dict

from oasis.social_platform.typing import ActionType


@dataclass
class ManualAction:
    r"""Some manual predefined social platform actions that need to be
    executed by certain agents.

    Args:
        agent_id: The ID of the agent that will perform the action.
        action: The action to perform.
        args: The arguments to pass to the action. For details of each args in
            each action, please refer to
            `https://github.com/camel-ai/oasis/blob/main/oasis/social_agent/agent_action.py`.
    """
    action_type: ActionType
    action_args: Dict[str, Any]

    def init(self, action_type, action_args):
        self.action_type = action_type
        self.action_args = action_args


@dataclass
class LLMAction:
    r"""Represents actions generated by a Language Learning Model (LLM)."""

    def init(self):
        pass
