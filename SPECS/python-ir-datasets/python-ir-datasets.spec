# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname ir-datasets

Name:           python-%{srcname}
Version:        0.5.11
Release:        %autorelease
Summary:        IR benchmark datasets for Python
License:        MIT
URL:            https://ir-datasets.com/
VCS:            git:https://github.com/allenai/ir_datasets
#!RemoteAsset
Source0:        https://files.pythonhosted.org/packages/source/i/ir_datasets/ir_datasets-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l ir_datasets

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(beautifulsoup4) >= 4.4.1
BuildRequires:  python3dist(ijson) >= 3.1.3
BuildRequires:  python3dist(inscriptis) >= 2.2
BuildRequires:  python3dist(lxml) >= 4.5.2
BuildRequires:  python3dist(lz4) >= 3.1.10
BuildRequires:  python3dist(numpy) >= 1.18.1
BuildRequires:  python3dist(pyarrow) >= 16.1
BuildRequires:  python3dist(pyyaml) >= 5.3.1
BuildRequires:  python3dist(requests) >= 2.22
BuildRequires:  python3dist(tqdm) >= 4.38
BuildRequires:  python3dist(trec-car-tools) >= 2.5.4
BuildRequires:  python3dist(unlzw3) >= 0.2.1
BuildRequires:  python3dist(warc3-wet) >= 0.2.3
BuildRequires:  python3dist(warc3-wet-clueweb09) >= 0.2.5
BuildRequires:  python3dist(zlib-state) >= 0.1.3

Provides:       python3-%{srcname}
%python_provide python3-%{srcname}

%description
ir-datasets provides reproducible access to common information retrieval datasets.

%files -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%{?autochangelog}
