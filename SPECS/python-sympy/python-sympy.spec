# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: CHEN Xuan <chenxuan@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sympy

Name:           python-%{srcname}
Version:        1.14.0
Release:        %autorelease
Summary:        A Python library for symbolic mathematics
License:        BSD-3-Clause AND MIT
URL:            https://www.sympy.org
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  isympy sympy

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(mpmath)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

Recommends:     python3dist(scipy)

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
SymPy aims to become a full-featured computer algebra system (CAS) while
keeping the code as simple as possible in order to be comprehensible and
easily extensible.  SymPy is written entirely in Python and does not require
any external libraries.

%check
# lack of some deps

%files -f %{pyproject_files}
%doc AUTHORS README.md
%{_bindir}/isympy
%{_mandir}/man1/isympy.1*

%changelog
%autochangelog
