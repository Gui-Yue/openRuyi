# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global common_description The Automated Testing Framework (ATF) is a collection of libraries to implement test programs in a variety of languages.

Name:           atf
Version:        0.23
Release:        %autorelease
Summary:        Automated Testing Framework (metapackage)
License:        BSD-2-Clause
URL:            https://github.com/freebsd/atf
#!RemoteAsset
Source:         https://github.com/freebsd/atf/archive/refs/tags/atf-%{version}.tar.gz
BuildSystem:    autotools

BuildOption(conf): INSTALL="install -p"
BuildOption(conf): --disable-static

BuildOption(build):   pkgtestsdir=%{_libexecdir}/atf/tests
BuildOption(build):   testsdir=%{_libexecdir}/atf/tests
BuildOption(install): pkgtestsdir=%{_libexecdir}/atf/tests
BuildOption(install): testsdir=%{_libexecdir}/atf/tests

BuildRequires:  automake gcc-c++ libtool make

%description
This is a metapackage for the Automated Testing Framework (ATF).
It ensures all core components are installed.


%package        tests
Summary:        Automated Testing Framework - Test suite
Requires:       libatf-c = %{version}
Requires:       libatf-c++ = %{version}
Requires:       libatf-sh = %{version}
Requires:       libatf-c-devel = %{version}
Requires:       libatf-c++-devel = %{version}
Requires:       libatf-sh-devel = %{version}

%description    tests
%{common_description}
This package installs the run-time tests for all the components of ATF.

%package -n     libatf-c
Summary:        Automated Testing Framework - C bindings

%description -n libatf-c
%{common_description}
This package provides the run-time libraries for tests using the ATF C bindings.

%package -n     libatf-c-devel
Summary:        Development files for ATF C bindings
Requires:       libatf-c = %{version}
%description -n libatf-c-devel
%{common_description}
This package provides the files to develop tests using the ATF C bindings.

%package -n     libatf-c++
Summary:        Automated Testing Framework - C++ bindings

%description -n libatf-c++
%{common_description}
This package provides the run-time libraries for tests using the ATF C++ bindings.

%package -n     libatf-c++-devel
Summary:        Development files for ATF C++ bindings
Requires:       libatf-c-devel = %{version}
Requires:       libatf-c++ = %{version}

%description -n libatf-c++-devel
%{common_description}
This package provides the files to develop tests using the ATF C++ bindings.

%package -n     libatf-sh
Summary:        Automated Testing Framework - POSIX shell bindings
Requires:       libatf-c++ = %{version}

%description -n libatf-sh
%{common_description}
This package provides the run-time libraries for tests using the ATF shell bindings.

%package -n     libatf-sh-devel
Summary:        Development files for ATF POSIX shell bindings
Requires:       libatf-sh = %{version}

%description -n libatf-sh-devel
%{common_description}
This package provides the files to develop tests using the ATF shell bindings.

%conf -p
autoreconf -is

%files
%doc %{_docdir}/atf

%files    tests
%{_libexecdir}/atf/tests
%{_mandir}/man7/atf.7*

%files -n libatf-c
%{_libdir}/libatf-c.so.1*
%{_mandir}/man1/atf-test-program.1*
%{_mandir}/man4/atf-test-case.4*
%{_mandir}/man3/atf-c.3*

%files -n libatf-c-devel
%{_datadir}/aclocal/atf-c.m4
%{_datadir}/aclocal/atf-common.m4
%{_includedir}/atf-c.h
%{_includedir}/atf-c/
%{_libdir}/libatf-c.so
%{_libdir}/pkgconfig/atf-c.pc

%files -n libatf-c++
%{_libdir}/libatf-c++.so.2*
%{_mandir}/man3/atf-c++.3*

%files -n libatf-c++-devel
%{_datadir}/aclocal/atf-c++.m4
%{_includedir}/atf-c++.hpp
%{_includedir}/atf-c++/
%{_libdir}/libatf-c++.so
%{_libdir}/pkgconfig/atf-c++.pc

%files -n libatf-sh
%{_bindir}/atf-sh
%dir %{_datadir}/atf
%{_datadir}/atf/
%{_libexecdir}/atf-check
%{_mandir}/man1/atf-sh.1*
%{_mandir}/man3/atf-sh.3*

%files -n libatf-sh-devel
%{_datadir}/aclocal/atf-sh.m4
%{_libdir}/pkgconfig/atf-sh.pc
%{_mandir}/man1/atf-check.1*

%changelog
%{?autochangelog}
