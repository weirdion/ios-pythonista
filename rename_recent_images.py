#!/usr/bin/env python3
import os
import tempfile

import photos
from objc_util import ObjCInstance

SHOULD_SAVE = True


def handle_image_assets():
    all_assets = photos.get_assets(media_type="image")

    with tempfile.TemporaryDirectory() as tmpdir:
        for a in all_assets:
            last_asset = ObjCInstance(a)
            file_name = str(last_asset.valueForKey_("filename"))

            # photo_lib_path = os.path.dirname(str(last_asset.pathForOriginalFile()))
            # print(f"Photo lib path: {photo_lib_path}")

            img = a.get_image()

            # print("\nCreated temporary directory", tmpdir)
            new_name = os.path.join(tmpdir, f"IMG_{a.creation_date.strftime('%Y%m%d_%H%M%S')}.jpeg")
            print(f"{file_name} -> {new_name}")
            img.save(new_name, "JPEG", quality=90, optimize=True, progressive=True)
            # print("\nPrinting DCIM\n {os.listdir(photo_lib_path)}")

            if SHOULD_SAVE and a.can_edit_content:
                # This only works if the Camera is set to save as JPG
                # For HEIC, this will throw an exception
                a.edit_content(new_name)


if __name__ == "__main__":
    handle_image_assets()
