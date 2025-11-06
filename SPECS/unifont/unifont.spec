# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           unifont
Version:        16.0.04
Release:        %autorelease
Summary:        Tools and glyph descriptions for the GNU Unifont fonts
License:        GPL-2.0-or-later AND OFL-1.1
URL:            https://unifoundry.com/unifont/index.html
# This project does not have a public VCS repository
#!RemoteAsset
Source0:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
#!RemoteAsset
Source1:        https://ftpmirror.gnu.org/gnu/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz.sig
BuildSystem:    autotools

BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl-GD
BuildRequires:  bdftopcf
BuildRequires:  bdf2psf
BuildRequires:  fontforge
BuildRequires:  texinfo

%description
A font with a glyph for every visible Unicode Basic Multilingual Plane code
point and more, with supporting utilities to modify the font.

This package contains tools and glyph descriptions.

%package     -n fonts-unifont
Summary:        GNU Unifont

%description -n fonts-unifont
A font with a glyph for every visible Unicode Basic Multilingual Plane code
point and more, with supporting utilities to modify the font.

%prep -a
# Disable rebuilding during installation
sed -i 's/^install: .*/install:/' Makefile
sed -i 's/install -s/install/' src/Makefile
# Disable imagemagick dependency
sed -i -E '/^compiled-files:/ s/[[:space:]]+thumbnails([[:space:]]+|$)/\1/g' font/Makefile

%conf
# No conf

%build -a
make -C font all ttf upperttf

%install -a
install -Dm 0644 font/compiled/unifont-%{version}.ttf %{buildroot}%{_datadir}/fonts/truetype/unifont/unifont.ttf

# Don't want these
find %{buildroot}/usr/share/unifont/ -type f \! -name %{name}.hex -delete
rm -rv %{buildroot}/usr/share/fonts/X11
rm %{buildroot}/usr/share/consolefonts/Unifont-APL8x16.psf.gz

# no tests.
%check

%files
%doc NEWS README
%license COPYING
%{_bindir}/*
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{_mandir}/man5/*

%files -n fonts-unifont
%{_datadir}/fonts/truetype/unifont/unifont.ttf
%{_datadir}/fonts/opentype/unifont/unifont*.otf

%changelog
%{?autochangelog}
