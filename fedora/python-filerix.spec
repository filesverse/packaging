Name:           python-filerix
Version:        1.0.0
Release:        1%{?dist}
Summary:        Python bindings for Filerix

License:        MIT
URL:            https://github.com/filesverse/python-filerix
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git, curl, tar, unzip, cmake, make, gcc-c++, python, systemd-devel, perl, perl-IPC-Cmd, perl-FindBin, perl-lib, perl-Pod-Usage, kernel-headers, kernel-devel
Requires:       python, filerix

%description
Python bindings for the Filerix file management library.

%prep
%autosetup -n %{name}-%{version}

%build
echo "Building python-filerix..."
make build

%install
make install PREFIX=%{buildroot}%{_prefix}

%files
%license LICENSE
%{_libdir}/python%{PYTHON_VERSION_MAJOR}.%{PYTHON_VERSION_MINOR}/site-packages/filerix*.so

%changelog
* Fri Feb 14 2025 KingMaj0r <kingmaj0r@hotmail.com> - 1.1.0-1
- Initial release
