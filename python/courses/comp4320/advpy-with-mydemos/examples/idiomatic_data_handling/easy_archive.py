#!/usr/bin/env python
import shutil

# Create an archive with a base name of ~/data_dir and .tar.gz extension
# compress the contents of the "../data" directory
shutil.make_archive('data_dir', 'gztar', "../data")


# Create an archive with a base name of ~/data_dir and .zip extension
# compress the contents of the "../data" directory
shutil.make_archive('data_dir', 'zip', "../data")
