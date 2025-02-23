Name:           node-filerix
Version:        1.1.1
Release:        1%{?dist}
Summary:        Node.js bindings for Filerix

License:        MIT
URL:            https://github.com/filesverse/node-filerix
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/microsoft/vcpkg/archive/refs/heads/master.tar.gz

BuildRequires:  git, curl, tar, unzip, cmake, make, gcc-c++, nodejs, npm, systemd-devel
Requires:       glibc, nodejs, filerix

%description
Node.js bindings for the Filerix file management library.

%prep
%autosetup -n %{name}-%{version}
tar -xzf %{SOURCE1} --strip-components=1 -C vcpkg

%build
echo "Building node-filerix..."
chmod +x scripts/build.sh
./scripts/build.sh %{buildroot} || { echo "Installation failed"; exit 1; }

%install
cmake --install build --prefix=%{buildroot}

%files
%license LICENSE
%{_libdir}/node_modules/filerix/filerix.node

%changelog
* Fri Feb 14 2025 KingMaj0r <kingmaj0r@hotmail.com> - 1.1.0-1
- Initial release
