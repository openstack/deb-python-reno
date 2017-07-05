# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

RELEASE_NOTES_SUBDIR = 'releasenotes'
NOTES_SUBDIR = 'notes'
PRELUDE_SECTION_NAME = 'prelude'
# This is a format string, so it needs to be formatted wherever it is used.
TEMPLATE = """\
---
{0}: >
    Replace this text with content to appear at the top of the section for this
    release. All of the prelude content is merged together and then rendered
    separately from the items listed in other parts of the file, so the text
    needs to be worded so that both the prelude and the other items make sense
    when read independently. This may mean repeating some details. Not every
    release note requires a prelude. Usually only notes describing major
    features or adding release theme details should have a prelude.
features:
  - |
    List new features here, or remove this section.  All of the list items in
    this section are combined when the release notes are rendered, so the text
    needs to be worded so that it does not depend on any information only
    available in another section, such as the prelude. This may mean repeating
    some details.
issues:
  - |
    List known issues here, or remove this section.  All of the list items in
    this section are combined when the release notes are rendered, so the text
    needs to be worded so that it does not depend on any information only
    available in another section, such as the prelude. This may mean repeating
    some details.
upgrade:
  - |
    List upgrade notes here, or remove this section.  All of the list items in
    this section are combined when the release notes are rendered, so the text
    needs to be worded so that it does not depend on any information only
    available in another section, such as the prelude. This may mean repeating
    some details.
deprecations:
  - |
    List deprecations notes here, or remove this section.  All of the list
    items in this section are combined when the release notes are rendered, so
    the text needs to be worded so that it does not depend on any information
    only available in another section, such as the prelude. This may mean
    repeating some details.
critical:
  - |
    Add critical notes here, or remove this section.  All of the list items in
    this section are combined when the release notes are rendered, so the text
    needs to be worded so that it does not depend on any information only
    available in another section, such as the prelude. This may mean repeating
    some details.
security:
  - |
    Add security notes here, or remove this section.  All of the list items in
    this section are combined when the release notes are rendered, so the text
    needs to be worded so that it does not depend on any information only
    available in another section, such as the prelude. This may mean repeating
    some details.
fixes:
  - |
    Add normal bug fixes here, or remove this section.  All of the list items
    in this section are combined when the release notes are rendered, so the
    text needs to be worded so that it does not depend on any information only
    available in another section, such as the prelude. This may mean repeating
    some details.
other:
  - |
    Add other notes here, or remove this section.  All of the list items in
    this section are combined when the release notes are rendered, so the text
    needs to be worded so that it does not depend on any information only
    available in another section, such as the prelude. This may mean repeating
    some details.
"""
