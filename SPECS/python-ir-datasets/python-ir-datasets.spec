# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ir-datasets
%global pypi_name ir_datasets

Name:           python-%{srcname}
Version:        0.5.11
Release:        %autorelease
Summary:        Common interface for information retrieval datasets
License:        Apache-2.0
URL:            https://ir-datasets.com/
VCS:            git:https://github.com/allenai/ir_datasets
#!RemoteAsset:  sha256:06c90af634ae5063c813286b35065debca1a974d26e136403d899f3ecd7ad463
Source0:        https://files.pythonhosted.org/packages/source/i/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools) >= 42
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(beautifulsoup4) >= 4.4.1
BuildRequires:  python3dist(inscriptis) >= 2.2.0
BuildRequires:  python3dist(lxml) >= 4.5.2
BuildRequires:  python3dist(numpy) >= 1.18.1
BuildRequires:  python3dist(pyyaml) >= 5.3.1
BuildRequires:  python3dist(requests) >= 2.22.0
BuildRequires:  python3dist(tqdm) >= 4.38.0
BuildRequires:  python3dist(trec-car-tools) >= 2.5.4
BuildRequires:  python3dist(lz4) >= 3.1.10
BuildRequires:  python3dist(warc3-wet) >= 0.2.3
BuildRequires:  python3dist(warc3-wet-clueweb09) >= 0.2.5
BuildRequires:  python3dist(zlib-state) >= 0.1.3
BuildRequires:  python3dist(ijson) >= 3.1.3
BuildRequires:  python3dist(unlzw3) >= 0.2.1
BuildRequires:  python3dist(pyarrow) >= 16.1.0

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
ir_datasets provides a common Python interface to information retrieval
benchmark datasets, training datasets, and related data resources.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
