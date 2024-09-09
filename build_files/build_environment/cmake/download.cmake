# SPDX-FileCopyrightText: 2021-2023 Blender Authors
#
# SPDX-License-Identifier: GPL-2.0-or-later

## Update and uncomment this in the release branch
set(BLENDER_VERSION 4.1)

function(download_source dep)
  set(TARGET_FILE ${${dep}_FILE})
  set(TARGET_HASH_TYPE ${${dep}_HASH_TYPE})
  set(TARGET_HASH ${${dep}_HASH})
  if(PACKAGE_USE_UPSTREAM_SOURCES)
    set(TARGET_URI  ${${dep}_URI})
  elseif(BLENDER_VERSION)
    set(TARGET_URI https://projects.blender.org/blender/lib-source/media/branch/blender-v${BLENDER_VERSION}-release/${TARGET_FILE})
  else()
    set(TARGET_URI https://projects.blender.org/blender/lib-source/media/branch/main/${TARGET_FILE})
  endif()
  # Validate all required variables are set and give an explicit error message
  # rather than CMake erroring out later on with a more ambigious error.
  if(NOT DEFINED TARGET_FILE)
    message(FATAL_ERROR "${dep}_FILE variable not set")
  endif()
  if(NOT DEFINED TARGET_HASH)
    message(FATAL_ERROR "${dep}_HASH variable not set")
  endif()
  if(NOT DEFINED TARGET_HASH_TYPE)
    message(FATAL_ERROR "${dep}_HASH_TYPE variable not set")
  endif()
  if(NOT DEFINED TARGET_URI)
    message(FATAL_ERROR "${dep}_URI variable not set")
  endif()
  set(TARGET_FILE ${PACKAGE_DIR}/${TARGET_FILE})
  message("Checking source : ${dep} (${TARGET_FILE})")
  if(NOT EXISTS ${TARGET_FILE})
    message("Checking source : ${dep} - source not found downloading from ${TARGET_URI}")
    file(
      DOWNLOAD ${TARGET_URI} ${TARGET_FILE}
      TIMEOUT 1800  # seconds
      EXPECTED_HASH ${TARGET_HASH_TYPE}=${TARGET_HASH}
      TLS_VERIFY ON
      SHOW_PROGRESS
    )
  endif()
  if(EXISTS ${TARGET_FILE})
    # Sometimes the download fails, but that is not a
    # fail condition for "file(DOWNLOAD" it will warn about
    # a CRC mismatch and just carry on, we need to explicitly
    # catch this and remove the bogus 0 byte file so we can
    # retry without having to go find the file and manually
    # delete it.
    file(SIZE ${TARGET_FILE} TARGET_SIZE)
    if(${TARGET_SIZE} EQUAL 0)
      file(REMOVE ${TARGET_FILE})
      message(FATAL_ERROR "for ${TARGET_FILE} file size 0, download likely failed, deleted...")
    endif()

    # If we are using sources from the blender repo also
    # validate that the hashes match, this takes a
    # little more time, but protects us when we are
    # building a release package and one of the packages
    # is missing or incorrect.
    #
    # For regular platform maintenaince this is not needed
    # since the actual build of the dep will notify the
    # platform maintainer if there is a problem with the
    # source package and refuse to build.
    if(NOT PACKAGE_USE_UPSTREAM_SOURCES OR FORCE_CHECK_HASH)
      file(${TARGET_HASH_TYPE} ${TARGET_FILE} LOCAL_HASH)
      if(NOT ${TARGET_HASH} STREQUAL ${LOCAL_HASH})
        message(FATAL_ERROR "${TARGET_FILE} ${TARGET_HASH_TYPE} mismatch\nExpected\t: ${TARGET_HASH}\nActual\t: ${LOCAL_HASH}")
      endif()
    endif()
  endif()
endfunction(download_source)

download_source(ZLIB)
download_source(OPENAL)
download_source(PNG)
download_source(JPEG)
download_source(BOOST)
download_source(BLOSC)
download_source(PTHREADS)
download_source(OPENEXR)
download_source(FREETYPE)
download_source(EPOXY)
download_source(ALEMBIC)
download_source(OPENSUBDIV)
download_source(SDL)
download_source(OPENCOLLADA)
download_source(OPENCOLORIO)
download_source(MINIZIPNG)
download_source(LLVM)
download_source(OPENMP)
download_source(OPENIMAGEIO)
download_source(TIFF)
download_source(OSL)
download_source(PYTHON)
download_source(TBB)
download_source(OPENVDB)
download_source(NUMPY)
download_source(LAME)
download_source(OGG)
download_source(VORBIS)
download_source(THEORA)
download_source(FLAC)
download_source(VPX)
download_source(OPUS)
download_source(X264)
download_source(OPENJPEG)
download_source(FFMPEG)
download_source(FFTW)
download_source(ICONV)
download_source(SNDFILE)
download_source(WEBP)
download_source(SPNAV)
download_source(JEMALLOC)
download_source(XML2)
download_source(YAMLCPP)
download_source(EXPAT)
download_source(PUGIXML)
download_source(FLEXBISON)
download_source(BZIP2)
download_source(FFI)
download_source(LZMA)
download_source(SSL)
download_source(SQLITE)
download_source(EMBREE)
download_source(USD)
download_source(MATERIALX)
download_source(OIDN)
download_source(LIBGLU)
download_source(MESA)
download_source(NASM)
download_source(XR_OPENXR_SDK)
download_source(WL_PROTOCOLS)
download_source(WAYLAND)
download_source(WAYLAND_LIBDECOR)
download_source(WAYLAND_WESTON)
download_source(ISPC)
download_source(GMP)
download_source(POTRACE)
download_source(HARU)
download_source(ZSTD)
download_source(SSE2NEON)
download_source(FLEX)
download_source(BROTLI)
download_source(FMT)
download_source(ROBINMAP)
download_source(IMATH)
download_source(PYSTRING)
download_source(OPENPGL)
download_source(LEVEL_ZERO)
download_source(DPCPP)
download_source(VCINTRINSICS)
download_source(OPENCLHEADERS)
download_source(ICDLOADER)
download_source(MP11)
download_source(SPIRV_HEADERS)
download_source(UNIFIED_RUNTIME)
download_source(IGC)
download_source(IGC_LLVM)
download_source(IGC_OPENCL_CLANG)
download_source(IGC_VCINTRINSICS)
download_source(IGC_SPIRV_HEADERS)
download_source(IGC_SPIRV_TOOLS)
download_source(IGC_SPIRV_TRANSLATOR)
download_source(GMMLIB)
download_source(OCLOC)
download_source(AOM)
download_source(FRIBIDI)
download_source(HARFBUZZ)
download_source(SHADERC)
download_source(SHADERC_SPIRV_TOOLS)
download_source(SHADERC_SPIRV_HEADERS)
download_source(SHADERC_GLSLANG)
download_source(VULKAN_HEADERS)
download_source(VULKAN_LOADER)
download_source(PYBIND11)
download_source(DEFLATE)