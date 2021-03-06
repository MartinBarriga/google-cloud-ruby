# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import synthtool as s
import synthtool.gcp as gcp
import synthtool.languages.ruby as ruby
import logging

AUTOSYNTH_MULTIPLE_COMMITS = True

logging.basicConfig(level=logging.DEBUG)

gapic = gcp.GAPICMicrogenerator()
library = gapic.ruby_library(
    "secretmanager", "v1",
    generator_args={
        "ruby-cloud-gem-name": "google-cloud-secret_manager",
        "ruby-cloud-title": "Secret Manager",
        "ruby-cloud-description": "Secret Manager is a secure and convenient storage system for API keys, passwords, certificates, and other sensitive data. Secret Manager provides a central place and single source of truth to manage, access, and audit secrets across Google Cloud.",
        "ruby-cloud-env-prefix": "SECRET_MANAGER",
        "ruby-cloud-wrapper-of": "v1:0.1;v1beta1:0.3",
        "ruby-cloud-product-url": "https://cloud.google.com/secret-manager",
        "ruby-cloud-api-id": "secretmanager",
    }
)

s.copy(library, merge=ruby.global_merge)
