# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname sentence-transformers
%global pypi_name sentence_transformers

Name:           python-%{srcname}
Version:        5.5.0
Release:        %autorelease
Summary:        Embeddings, retrieval, and reranking
License:        Apache-2.0
URL:            https://www.sbert.net/
VCS:            git:https://github.com/huggingface/sentence-transformers
#!RemoteAsset:  sha256:9cec675e68bfe09d07466d1f13ab06d1d79d60a0f45b154baf433bde6ae159cb
Source0:        https://files.pythonhosted.org/packages/source/s/%{srcname}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    pyproject

BuildOption(install):  -l %{pypi_name}

BuildRequires:  pkgconfig(python3)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(transformers) >= 4.41
BuildRequires:  python3dist(huggingface-hub) >= 0.23
BuildRequires:  python3dist(torch) >= 1.11
BuildRequires:  python3dist(numpy) >= 1.20
BuildRequires:  python3dist(scikit-learn) >= 0.22
BuildRequires:  python3dist(scipy) >= 1.0
BuildRequires:  python3dist(typing-extensions) >= 4.5
BuildRequires:  python3dist(tqdm) >= 4.0

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Sentence Transformers provides tools for text embeddings, semantic search,
clustering, retrieval, and reranking.

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md NOTICE.txt
%license LICENSE

%changelog
%autochangelog
