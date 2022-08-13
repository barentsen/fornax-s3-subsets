"""
test parameters for a series of full TESSCut cubes. these are massive
(35-115 GB) 4-dimensional uncompressed rasters.
"""
# this series of shapes is intended to demonstrate the huge performance
# differences caused by 'orientation' in a >2D FITS array.
# note that the last axis is only length 2.
CUT_SHAPES = ((1, 100, 100, 1), (100, 100, 1, 1), (100, 1, 100, 1))
CUT_COUNTS = (1, 5)
BUCKET = "stpubdata"
AUTHENTICATE_S3 = False
HDU_IX = 1
# these files are too big to open with other loaders.
# a 'greedy' loader would require at least 120 GB of
# available RAM for some of these files. This would drop
# to a mere ~40 GB for astropy_s3 (s3 access without section,
# copies an entire HDU into memory), but would still require using
# a rather expensive instance. fitsio simply won't work at all --
# CFITSIO throws an error when it simply _thinks_ about opening
# one of these files, before transferring any data at all.
LOADERS = ("astropy", "astropy_s3_section")
TEST_FILES = (
    "tess/public/mast/tess-s0026-4-1-cube.fits",
    "tess/public/mast/tess-s0052-2-3-cube.fits",
    "tess/public/mast/tess-s0035-3-2-cube.fits",
    "tess/public/mast/tess-s0050-1-3-cube.fits",
    "tess/public/mast/tess-s0002-3-2-cube.fits",
    "tess/public/mast/tess-s0043-2-2-cube.fits",
    "tess/public/mast/tess-s0016-2-4-cube.fits",
    "tess/public/mast/tess-s0021-3-4-cube.fits",
    "tess/public/mast/tess-s0035-1-3-cube.fits",
    "tess/public/mast/tess-s0031-2-4-cube.fits",
    "tess/public/mast/tess-s0008-2-2-cube.fits",
    "tess/public/mast/tess-s0008-4-3-cube.fits",
    "tess/public/mast/tess-s0010-1-1-cube.fits",
    "tess/public/mast/tess-s0032-3-3-cube.fits",
    "tess/public/mast/tess-s0029-1-1-cube.fits",
    "tess/public/mast/tess-s0020-3-1-cube.fits",
    "tess/public/mast/tess-s0018-3-4-cube.fits",
    "tess/public/mast/tess-s0050-2-1-cube.fits",
    "tess/public/mast/tess-s0035-1-2-cube.fits",
    "tess/public/mast/tess-s0022-4-1-cube.fits",
    "tess/public/mast/tess-s0005-2-3-cube.fits",
    "tess/public/mast/tess-s0007-2-3-cube.fits",
    "tess/public/mast/tess-s0003-2-3-cube.fits",
    "tess/public/mast/tess-s0042-4-2-cube.fits",
    "tess/public/mast/tess-s0051-2-2-cube.fits",
    "tess/public/mast/tess-s0022-3-3-cube.fits",
    "tess/public/mast/tess-s0014-1-1-cube.fits",
    "tess/public/mast/tess-s0018-4-3-cube.fits",
    "tess/public/mast/tess-s0037-3-4-cube.fits",
    "tess/public/mast/tess-s0010-2-3-cube.fits",
    "tess/public/mast/tess-s0046-1-2-cube.fits",
    "tess/public/mast/tess-s0032-1-3-cube.fits",
    "tess/public/mast/tess-s0017-3-1-cube.fits",
    "tess/public/mast/tess-s0051-1-3-cube.fits",
    "tess/public/mast/tess-s0052-2-1-cube.fits",
    "tess/public/mast/tess-s0036-2-4-cube.fits",
    "tess/public/mast/tess-s0017-1-4-cube.fits",
    "tess/public/mast/tess-s0001-4-2-cube.fits",
    "tess/public/mast/tess-s0006-4-2-cube.fits",
    "tess/public/mast/tess-s0025-3-3-cube.fits",
    "tess/public/mast/tess-s0048-2-2-cube.fits",
    "tess/public/mast/tess-s0010-2-4-cube.fits",
    "tess/public/mast/tess-s0039-2-4-cube.fits",
    "tess/public/mast/tess-s0053-1-4-cube.fits",
    "tess/public/mast/tess-s0029-4-3-cube.fits",
    "tess/public/mast/tess-s0048-4-4-cube.fits",
    "tess/public/mast/tess-s0002-1-4-cube.fits",
    "tess/public/mast/tess-s0050-2-1-cube.fits",
    "tess/public/mast/tess-s0027-4-2-cube.fits",
    "tess/public/mast/tess-s0012-4-1-cube.fits",
    "tess/public/mast/tess-s0038-4-4-cube.fits",
    "tess/public/mast/tess-s0011-4-4-cube.fits",
    "tess/public/mast/tess-s0022-3-1-cube.fits",
    "tess/public/mast/tess-s0001-2-3-cube.fits",
    "tess/public/mast/tess-s0007-1-3-cube.fits",
    "tess/public/mast/tess-s0029-1-3-cube.fits",
    "tess/public/mast/tess-s0009-1-4-cube.fits",
    "tess/public/mast/tess-s0046-4-2-cube.fits",
    "tess/public/mast/tess-s0026-3-4-cube.fits",
    "tess/public/mast/tess-s0014-1-2-cube.fits",
    "tess/public/mast/tess-s0033-1-3-cube.fits",
    "tess/public/mast/tess-s0050-4-1-cube.fits",
    "tess/public/mast/tess-s0010-1-2-cube.fits",
    "tess/public/mast/tess-s0030-2-1-cube.fits",
    "tess/public/mast/tess-s0023-1-4-cube.fits",
    "tess/public/mast/tess-s0029-3-3-cube.fits",
    "tess/public/mast/tess-s0050-1-2-cube.fits",
    "tess/public/mast/tess-s0029-3-4-cube.fits",
    "tess/public/mast/tess-s0045-3-4-cube.fits",
    "tess/public/mast/tess-s0024-1-4-cube.fits",
    "tess/public/mast/tess-s0026-1-4-cube.fits",
    "tess/public/mast/tess-s0032-3-4-cube.fits",
    "tess/public/mast/tess-s0028-3-1-cube.fits",
    "tess/public/mast/tess-s0029-2-2-cube.fits",
    "tess/public/mast/tess-s0026-3-2-cube.fits",
    "tess/public/mast/tess-s0048-2-4-cube.fits",
    "tess/public/mast/tess-s0025-2-3-cube.fits",
    "tess/public/mast/tess-s0051-2-3-cube.fits",
    "tess/public/mast/tess-s0001-2-4-cube.fits",
    "tess/public/mast/tess-s0033-3-4-cube.fits",
    "tess/public/mast/tess-s0012-3-3-cube.fits",
    "tess/public/mast/tess-s0033-3-4-cube.fits",
    "tess/public/mast/tess-s0030-4-1-cube.fits",
    "tess/public/mast/tess-s0006-1-2-cube.fits",
    "tess/public/mast/tess-s0044-2-1-cube.fits",
    "tess/public/mast/tess-s0029-2-3-cube.fits",
    "tess/public/mast/tess-s0039-4-3-cube.fits",
    "tess/public/mast/tess-s0034-1-1-cube.fits",
    "tess/public/mast/tess-s0019-1-3-cube.fits",
    "tess/public/mast/tess-s0024-2-4-cube.fits",
    "tess/public/mast/tess-s0040-1-2-cube.fits",
    "tess/public/mast/tess-s0034-3-4-cube.fits",
    "tess/public/mast/tess-s0053-3-2-cube.fits",
    "tess/public/mast/tess-s0015-1-4-cube.fits",
    "tess/public/mast/tess-s0001-2-1-cube.fits",
    "tess/public/mast/tess-s0046-4-1-cube.fits",
    "tess/public/mast/tess-s0004-2-3-cube.fits",
    "tess/public/mast/tess-s0019-4-4-cube.fits",
    "tess/public/mast/tess-s0044-2-4-cube.fits",
    "tess/public/mast/tess-s0036-3-2-cube.fits",
)
