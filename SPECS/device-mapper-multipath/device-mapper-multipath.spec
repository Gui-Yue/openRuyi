# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           device-mapper-multipath
Version:        0.13.0
Release:        %autorelease
Summary:        Tools to manage multipath devices using device-mapper
License:        GPL-2.0-only AND GPL-3.0-only
URL:            http://christophe.varoqui.free.fr/
VCS:            git:https://github.com/opensvc/multipath-tools
#!RemoteAsset
Source0:        https://github.com/opensvc/multipath-tools/archive/refs/tags/%{version}.tar.gz
BuildSystem:    autotools

BuildOption(build):  LIB=%{_lib}
BuildOption(install):  bindir=%{_bindir}
BuildOption(install):  syslibdir=%{_libdir}
BuildOption(install):  usrlibdir=%{_libdir}
BuildOption(install):  plugindir=%{_libdir}/multipath
BuildOption(install):  mandir=%{_mandir}
BuildOption(install):  unitdir=%{_unitdir}
BuildOption(install):  includedir=%{_includedir}
BuildOption(install):  pkgconfdir=%{_libdir}/pkgconfig
BuildOption(install):  tmpfilesdir=%{_tmpfilesdir}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libaio)
BuildRequires:  device-mapper-devel >= 1.02.89
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  libsepol-devel
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd-rpm-macros
BuildRequires:  json-c-devel
BuildRequires:  userspace-rcu-devel
BuildRequires:  pkgconfig(mount)

Requires:       %{name}-libs = %{version}-%{release}
Requires:       kpartx = %{version}-%{release}
Requires:       device-mapper >= 1.02.96
Requires:       userspace-rcu
Requires:       readline
Requires:       libmount
Requires:       systemd

%description
device-mapper-multipath provides tools to manage multipath devices by
instructing the device-mapper multipath kernel module what to do.

%package        libs
Summary:        The %{name} modules and shared library

%description    libs
The %{name}-libs provides the path checker and prioritizer modules.

%package        devel
Summary:        Development libraries and headers for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
Development headers for device-mapper-multipath.

%package     -n kpartx
Summary:        Partition device manager for device-mapper devices

%description -n kpartx
kpartx manages partition creation and removal for device-mapper devices.

%package     -n libdmmp
Summary:        device-mapper-multipath C API library
Requires:       %{name}-libs = %{version}-%{release}

%description -n libdmmp
C API library for device-mapper-multipath.

%package     -n libdmmp-devel
Summary:        device-mapper-multipath C API library headers
Requires:       libdmmp = %{version}-%{release}
Requires:       pkgconfig

%description -n libdmmp-devel
Development headers for libdmmp.

# No configure.
%conf

%install -a
install -d %{buildroot}/etc/multipath
rm -rf %{buildroot}/%{_initrddir}

%post
%systemd_post multipathd.service

%preun
%systemd_preun multipathd.service

%postun
if [ $1 -ge 1 ] ; then
	%{_sbindir}/multipathd forcequeueing daemon > /dev/null 2>&1 || :
fi
%systemd_postun_with_restart multipathd.service

%files
%license LICENSES/GPL-2.0 LICENSES/LGPL-2.0 LICENSES/GPL-3.0
%doc README.md
%{_bindir}/multipath
%{_bindir}/multipathd
%{_bindir}/multipathc
%{_bindir}/mpathpersist
%{_unitdir}/multipathd.service
%{_unitdir}/multipathd-queueing.service
%{_unitdir}/multipathd.socket
%{_mandir}/man5/multipath.conf.5*
%{_mandir}/man8/multipath.8*
%{_mandir}/man8/multipathd.8*
%{_mandir}/man8/multipathc.8*
%{_mandir}/man8/mpathpersist.8*
%{_udevrulesdir}/56-multipath.rules
%{_udevrulesdir}/11-dm-mpath.rules
%{_udevrulesdir}/99-z-dm-mpath-late.rules
%{_tmpfilesdir}/multipath.conf
%dir /etc/multipath

%files libs
%license LICENSES/GPL-2.0 LICENSES/LGPL-2.0 LICENSES/LGPL-2.1
%{_libdir}/libmultipath.so
%{_libdir}/libmultipath.so.*
%{_libdir}/libmpathutil.so
%{_libdir}/libmpathutil.so.*
%{_libdir}/libmpathpersist.so.*
%{_libdir}/libmpathcmd.so.*
%{_libdir}/libmpathvalid.so.*
%dir %{_libdir}/multipath
%{_libdir}/multipath/*

%files devel
%{_libdir}/libmpathpersist.so
%{_libdir}/libmpathcmd.so
%{_libdir}/libmpathvalid.so
%{_includedir}/mpath_cmd.h
%{_includedir}/mpath_persist.h
%{_includedir}/mpath_valid.h
%{_mandir}/man3/mpath_persistent_reserve_in.3*
%{_mandir}/man3/mpath_persistent_reserve_out.3*

%files -n kpartx
%license LICENSES/GPL-2.0
%{_bindir}/kpartx
%{_prefix}/lib/udev/kpartx_id
%{_mandir}/man8/kpartx.8*
%{_udevrulesdir}/11-dm-parts.rules
%{_udevrulesdir}/66-kpartx.rules
%{_udevrulesdir}/68-del-part-nodes.rules

%files -n libdmmp
%license LICENSES/GPL-3.0
%{_libdir}/libdmmp.so.*

%files -n libdmmp-devel
%{_libdir}/libdmmp.so
%{_includedir}/libdmmp/
%{_mandir}/man3/dmmp_*
%{_mandir}/man3/libdmmp.h.3*
%{_libdir}/pkgconfig/libdmmp.pc

%changelog
%{?autochangelog}
