# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""FedJAX experimental types."""

from typing import Mapping, Union
import jax.numpy as jnp

# The difference between Batch* and Single* is Single* is a mapping to a SINGLE
# example; where as Batch* is to a batch of N examples.
BatchExample = Mapping[str, jnp.ndarray]
SingleExample = Mapping[str, jnp.ndarray]

BatchPrediction = Union[jnp.ndarray, Mapping[str, jnp.ndarray]]
SinglePrediction = Union[jnp.ndarray, Mapping[str, jnp.ndarray]]
