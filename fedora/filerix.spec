Name:           filerix
Version:        1.0.3
Release:        1%{?dist}
Summary:        A high-performance file management library

License:        MIT
URL:            https://github.com/filesverse/filerix
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/microsoft/vcpkg/archive/refs/heads/master.tar.gz

BuildRequires:  git, curl, tar, unzip, cmake, make, systemd-devel, gcc-c++
Requires:       glibc, udev

%description
Filerix is a lightweight and high-performance file management library 
designed to provide essential file system operations.

%package devel
Summary:        Development files for Filerix
Requires:       %{name} = %{version}-%{release}

%description devel
The Filerix development package contains headers and pkg-config files needed 
to develop applications using the Filerix library.

%prep
%autosetup -n %{name}-%{version}
tar -xzf %{SOURCE1} --strip-components=1 -C vcpkg

%build
echo "Building node-filerix..."
chmod +x scripts/build.sh
./scripts/build.sh || { echo "Installation failed"; exit 1; }

%install
mkdir -p %{buildroot}%{_libdir}
install -m 755 ./build/src/libfilerix.so %{buildroot}%{_libdir}/libfilerix.so
cmake --install build --prefix=%{buildroot}

%files
%license LICENSE
%doc README.md
%{_libdir}/libfilerix.so

%files devel
%{_includedir}/filerix/*
%{_libdir}/pkgconfig/filerix.pc

%changelog
* Fri Feb 14 2025 KingMaj0r <kingmaj0r@hotmail.com> - 1.0.1-1
- Updated build process to use CMake and Vcpkg for dependencies
- Added CMake integration to the RPM build
* Fri Feb 14 2025 KingMaj0r <kingmaj0r@hotmail.com> - 1.0.0-1
- Initial release
