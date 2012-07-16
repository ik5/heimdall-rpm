Name:		heimdall
Version:	1.3.1
Release:	0.0.git.20110916.fbbed42c1e%{?dist}
Summary:	Software for flashing Galaxy S

License:	MIT
URL:		http://www.glassechidna.com.au/products/heimdall/
Source0:	%{name}-%{version}.tar.gz
# Patch0:		heimdall.no_udevadm_during_build.patch

BuildRequires:	libpit-devel libpit-static libusb1-devel gcc-c++

%description
This software attempts to flash your Galaxy S device

DISCLAIMER:

    This software attempts to flash your Galaxy S device. The very nature of
    flashing is dangerous. As with all flashing software, Heimdall has the
    potential to damage (brick) your phone if not used carefully. If you're
    concerned, don't use this software. Flashing ROMs onto your phone may also
    void your warranty. Benjamin Dobell and Glass Echidna are not responsible
    for the result of your actions.

%prep
%setup -q -n heimdall
# %patch0

# This is static linking :-(
sed -i 's,../libpit/libpit-1.3.a,%{_libdir}/libpit-1.3.a,;' Makefile.in

%build

# Use system's libusb1 instead of the one included upstream
# Autoconf should actually have set -fPIC for us
export CXXFLAGS="-fPIC -I%{_includedir}/libusb-1.0"

%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf %buildroot
make install DESTDIR=%buildroot


%post
/sbin/udevadm control --reload-rules

%postun
/sbin/udevadm control --reload-rules

%files
%doc doc-pak/*
%{_bindir}/heimdall
/lib/udev/rules.d/60-heimdall-galaxy-s.rules

%changelog
* Mon Jul 16 2012 Ido Kanner <idokan@gmail.com> 1.3.1-0.0.git.20110916.fbbed42c1e
- First attempt

* Wed Aug 17 2011 Ingvar Hagelund <ingvar@redpill-linpro.com> 1.3-0.0.git.20110817.ed9b08e5
- First cut of an rpm set for heimdall

