# =========================================================================
# Copyright 2020 Viktor Borzov

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#========================================================================== 

from bin.main.ui_manager import UIManager
from bin.main.watcher import Watcher
from bin.utilities.update_manager import UpdateManager

if __name__ == "__main__":
    watcher = Watcher()
    um = UpdateManager()
    ui_manager = UIManager(um)
    
    watcher.add_manga_observer(ui_manager.manga_changes)
    watcher.add_sites_observer(ui_manager.manga_sites)
    watcher.add_latest_observer(ui_manager.latests)

    watcher.watch()
    ui_manager.start()