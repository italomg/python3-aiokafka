%global sname aiokafka
%global owner aio-libs

Name:       python-%{sname}
Version:    0.7.2
Release:    1%{?dist}
Summary:    Asyncio client for Kafka
License:    ASL 2.0
Source0:    https://github.com/%{owner}/%{sname}/archive/refs/tags/v%{version}.tar.gz
URL:        https://github.com/%{owner}/%{sname}
BuildArch:  noarch

BuildRequires:  python3-devel python3-wheel
Requires:       python3

%description
%{summary}

%package -n python3-%{sname}
Summary:    %{summary}

%description -n python3-%{sname}
%{summary}

%prep
%autosetup -p1 -n %{sname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{sname}

%check
AIOKAFKA_NO_EXTENSIONS=1 python -m pytest -s tests

%files -n python3-%{sname} -f %{pyproject_files}
%license LICENSE
%doc README.rst

%changelog
* Tue Jul 12 2022 Italo Garcia <italo.garcia@aiven.io> - 0.7.2-1
- Initial package
