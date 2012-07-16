Name:		heimdall-frontend
Version:	1.3.1
Release:	0.0.git.20110916.fbbed42c1e%{?dist}
Summary:	QT frontend for heimdall

License:	MIT
URL:		http://www.glassechidna.com.au/products/heimdall/
Source0:	heimdall-%{version}.tar.gz

BuildRequires:	qt-devel

%description
QT frontend for heimdall

DISCLAIMER:

    This software attempts to flash your Galaxy S device. The very nature of
    flashing is dangerous. As with all flashing software, Heimdall has the
    potential to damage (brick) your phone if not used carefully. If you're
    concerned, don't use this software. Flashing ROMs onto your phone may also
    void your warranty. Benjamin Dobell and Glass Echidna are not responsible
    for the result of your actions.

%prep
%setup -q -n heimdall-frontend
head -20 Source/main.cpp > LICENSE

# This is static linking :-(
sed -i 's,../libpit/libpit-1.3.a,%{_libdir}/libpit-1.3.a,;' heimdall-frontend.pro

%build

qmake-qt4 OUTPUTDIR=/usr/bin
make %{?_smp_mflags} 


%install
rm -rf %buildroot
make install INSTALL_ROOT=%{buildroot}


%files
%doc LICENSE
%{_bindir}/heimdall-frontend


%changelog
* Mon Jul 16 2012 Ido Kanner <idokan@gmail.com> 1.3.1-0.0.git.20110916.fbbed42c1e
- First attempt

* Wed Aug 17 2011 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.3-0.0.git.20110817.ed9b08e5
- First cut of an rpm set for heimdall
