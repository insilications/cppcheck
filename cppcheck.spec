#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cppcheck
Version  : 2.2
Release  : 32
URL      : https://github.com/danmar/cppcheck/archive/2.2/cppcheck-2.2.tar.gz
Source0  : https://github.com/danmar/cppcheck/archive/2.2/cppcheck-2.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: cppcheck-bin = %{version}-%{release}
Requires: cppcheck-data = %{version}-%{release}
Requires: cppcheck-license = %{version}-%{release}
Requires: Pygments
BuildRequires : Pygments
BuildRequires : Z3-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-qmake
BuildRequires : glibc-dev
BuildRequires : python3
BuildRequires : qtbase-dev mesa-dev

%description
# Cppcheck
| Linux ビルド状態 | Windows ビルド状態 | Coverity Scan Build 状態 |
|:--:|:--:|:--:|
| [![Linux ビルド状態](https://img.shields.io/travis/danmar/cppcheck/master.svg?label=Linux%20build)](https://travis-ci.org/danmar/cppcheck) | [![Windows ビルド状態](https://img.shields.io/appveyor/ci/danmar/cppcheck/master.svg?label=Windows%20build)](https://ci.appveyor.com/project/danmar/cppcheck/branch/master) | [![Coverity Scan Build 状態](https://img.shields.io/coverity/scan/512.svg)](https://scan.coverity.com/projects/512) |

%package bin
Summary: bin components for the cppcheck package.
Group: Binaries
Requires: cppcheck-data = %{version}-%{release}
Requires: cppcheck-license = %{version}-%{release}

%description bin
bin components for the cppcheck package.


%package data
Summary: data components for the cppcheck package.
Group: Data

%description data
data components for the cppcheck package.


%package license
Summary: license components for the cppcheck package.
Group: Default

%description license
license components for the cppcheck package.


%prep
%setup -q -n cppcheck-2.2
cd %{_builddir}/cppcheck-2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601997849
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1601997849
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cppcheck
cp %{_builddir}/cppcheck-2.2/COPYING %{buildroot}/usr/share/package-licenses/cppcheck/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/cppcheck-2.2/externals/simplecpp/LICENSE %{buildroot}/usr/share/package-licenses/cppcheck/49d4c0ce1a16601f1e265d446b6c5ea6b512f27c
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cppcheck

%files data
%defattr(-,root,root,-)
/usr/share/Cppcheck/addons/__init__.py
/usr/share/Cppcheck/addons/cert.py
/usr/share/Cppcheck/addons/cppcheckdata.py
/usr/share/Cppcheck/addons/findcasts.py
/usr/share/Cppcheck/addons/misc.py
/usr/share/Cppcheck/addons/misra.py
/usr/share/Cppcheck/addons/naming.py
/usr/share/Cppcheck/addons/namingng.py
/usr/share/Cppcheck/addons/threadsafety.py
/usr/share/Cppcheck/addons/y2038.py
/usr/share/Cppcheck/cfg/avr.cfg
/usr/share/Cppcheck/cfg/boost.cfg
/usr/share/Cppcheck/cfg/bsd.cfg
/usr/share/Cppcheck/cfg/cairo.cfg
/usr/share/Cppcheck/cfg/cppcheck-lib.cfg
/usr/share/Cppcheck/cfg/cppunit.cfg
/usr/share/Cppcheck/cfg/daca.cfg
/usr/share/Cppcheck/cfg/embedded_sql.cfg
/usr/share/Cppcheck/cfg/emscripten.cfg
/usr/share/Cppcheck/cfg/gnu.cfg
/usr/share/Cppcheck/cfg/googletest.cfg
/usr/share/Cppcheck/cfg/gtk.cfg
/usr/share/Cppcheck/cfg/icu.cfg
/usr/share/Cppcheck/cfg/kde.cfg
/usr/share/Cppcheck/cfg/libcerror.cfg
/usr/share/Cppcheck/cfg/libcurl.cfg
/usr/share/Cppcheck/cfg/libsigc++.cfg
/usr/share/Cppcheck/cfg/lua.cfg
/usr/share/Cppcheck/cfg/mfc.cfg
/usr/share/Cppcheck/cfg/microsoft_atl.cfg
/usr/share/Cppcheck/cfg/microsoft_sal.cfg
/usr/share/Cppcheck/cfg/microsoft_unittest.cfg
/usr/share/Cppcheck/cfg/motif.cfg
/usr/share/Cppcheck/cfg/nspr.cfg
/usr/share/Cppcheck/cfg/opencv2.cfg
/usr/share/Cppcheck/cfg/opengl.cfg
/usr/share/Cppcheck/cfg/openmp.cfg
/usr/share/Cppcheck/cfg/openssl.cfg
/usr/share/Cppcheck/cfg/posix.cfg
/usr/share/Cppcheck/cfg/python.cfg
/usr/share/Cppcheck/cfg/qt.cfg
/usr/share/Cppcheck/cfg/ruby.cfg
/usr/share/Cppcheck/cfg/sdl.cfg
/usr/share/Cppcheck/cfg/sfml.cfg
/usr/share/Cppcheck/cfg/sqlite3.cfg
/usr/share/Cppcheck/cfg/std.cfg
/usr/share/Cppcheck/cfg/tinyxml2.cfg
/usr/share/Cppcheck/cfg/windows.cfg
/usr/share/Cppcheck/cfg/wxwidgets.cfg
/usr/share/Cppcheck/cfg/zlib.cfg
/usr/share/Cppcheck/platforms/aix_ppc64.xml
/usr/share/Cppcheck/platforms/arm32-wchar_t2.xml
/usr/share/Cppcheck/platforms/arm32-wchar_t4.xml
/usr/share/Cppcheck/platforms/arm64-wchar_t2.xml
/usr/share/Cppcheck/platforms/arm64-wchar_t4.xml
/usr/share/Cppcheck/platforms/avr8.xml
/usr/share/Cppcheck/platforms/cray_sv1.xml
/usr/share/Cppcheck/platforms/msp430_eabi_large_datamodel.xml
/usr/share/Cppcheck/platforms/unix32-unsigned.xml
/usr/share/Cppcheck/platforms/unix64-unsigned.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cppcheck/49d4c0ce1a16601f1e265d446b6c5ea6b512f27c
/usr/share/package-licenses/cppcheck/8624bcdae55baeef00cd11d5dfcfa60f68710a02
