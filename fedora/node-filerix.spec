Name:           node-filerix
Version:        1.1.2
Release:        1%{?dist}
Summary:        Node.js bindings for Filerix

License:        MIT
URL:            https://github.com/filesverse/node-filerix
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  git, curl, tar, unzip, cmake, make, gcc-c++, nodejs, npm, systemd-devel, chrpath
Requires:       nodejs, filerix

%description
Node.js bindings for the Filerix file management library.

%prep
%autosetup -n %{name}-%{version}

%build
echo "Building node-filerix..."
make build

%install
make install PREFIX=%{buildroot}%{_prefix}

%files
%license LICENSE
%{_libdir}/node_modules/filerix/filerix.node

%changelog
* Fri Feb 14 2025 KingMaj0r <kingmaj0r@hotmail.com> - 1.1.0-1
- Initial release
