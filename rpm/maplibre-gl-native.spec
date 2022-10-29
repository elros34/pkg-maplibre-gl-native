Summary: Maplibre GL Native Qt version
Name: qmaplibregl
Version: 2.0.1.0
Release: 1%{?dist}
License: BSD-2-Clause
Group: Libraries/Geosciences
URL: https://github.com/maplibre/maplibre-gl-native

Source: %{name}-%{version}.tar.gz
Patch1: 0001-Switch-to-CURL-for-downloads.patch
Patch2: 0002-Add-long-int-to-toString.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(icu-uc)
Conflicts: qmapboxgl
Obsoletes: qmapboxgl

Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
A library for embedding interactive, customizable vector maps into native applications on multiple platforms.
It takes stylesheets that conform to the Mapbox Style Specification, applies them to vector tiles that
conform to the Mapbox Vector Tile Specification, and renders them using OpenGL.

MapLibre GL Native is a community led fork derived from mapbox-gl-native.

PackageName: Maplibre GL Native Qt
PackagerName: rinigus
Categories:
  - Library
  - Maps
  - Science
Icon: https://raw.githubusercontent.com/maplibre/maplibre.github.io/main/img/maplibre-logo-dark.svg
  
%package devel
Summary:        Development files for %{name}
License:        Open Source
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers for %{name}.

%prep
%setup -q -n %{name}-%{version}/maplibre-gl-native
%patch1 -p1
%patch2 -p1

%build
%cmake -DMBGL_WITH_QT=ON -DMBGL_WITH_WERROR=OFF -DCMAKE_INSTALL_PREFIX:PATH=/usr -DMBGL_QT_WITH_HEADLESS=OFF -DMBGL_QT_LIBRARY_ONLY=ON -DMBGL_QT_STATIC=OFF -DMBGL_QT_WITH_INTERNAL_ICU=ON .
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
mkdir -p %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root, 0755)
%{_libdir}/libQMapLibreGL.so.*

%files devel
%{_includedir}/mbgl
%{_includedir}/QMapLibreGL
#%{_libdir}/libQMapboxGL.a
%{_libdir}/libQMapLibreGL.so
%{_libdir}/cmake/QMapLibreGL

%changelog
* Sun Dec 5 2021 rinigus <rinigus.git@gmail.com> - 2.0.0-1
- switch to maplibre

* Sat Mar 10 2018 rinigus <rinigus.git@gmail.com> - 1.3.0-1
- update to the current upstream version

* Sat Sep 9 2017 rinigus <rinigus.git@gmail.com> - 1.1.0-1
- initial packaging release for SFOS
