%define soversion 1

Name:		libpit
Version:	1.3.1
Release:	0.0.git.20110916.fbbed42c1e%{?dist}
Summary:	Library for heimdall

License:	MIT
URL:		http://www.glassechidna.com.au/products/heimdall/
Source0:	heimdall-%{version}.tar.gz

BuildRequires:	gcc-c++


%description
%{name} is a library used by heimdall

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package	static
Summary:	Static libraries for %{name}
Requires:	%{name} = %{version}-%{release}

%description	static
The %{name}-static package contains static libraries for static linking of
applications that use %{name}.


%prep
%setup -q -n %{name}


%build
# Autoconf should actually have set -fPIC for us
export CXXFLAGS="-fPIC %optflags"

%configure --disable-static
make %{?_smp_mflags}

# Upstream does not build shared libs(!)
pushd Source
gcc -shared %{name}.o -lc -Wl,-soname -Wl,%{name}.so.%{soversion} -o %{name}.so.%{version}
%{__ln_s} %{name}.so.%{version} %{name}.so.%{soversion}
popd

head -20 Source/%{name}.cpp > LICENSE

%install
rm -rf %buildroot
make install DESTDIR=%buildroot 
mkdir %{buildroot}%{_includedir}
%__install -D -m 0644 Source/*.h %{buildroot}%{_includedir}
%__cp -a Source/*.so.* %{buildroot}%{_libdir}
find %buildroot -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc LICENSE
%{_libdir}/*.so.*

%files devel
%doc LICENSE
%{_includedir}/*

%files static
%doc LICENSE
%{_libdir}/*.a


%changelog
* Mon Jul 16 2012 Ido Kanner <idokan@gmail.com> 1.3.1-0.0.git.20110916.fbbed42c1e
- First attempt

* Wed Aug 17 2011 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.3-0.0.git.20110817.ed9b08e5
- First cut of an rpm set of heimdall
