# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       device-mapper

# >> macros
# << macros

Summary:    Device mapper utility
Version:    1.02.76
Release:    1
Group:      System/Base
License:    GPLv2
URL:        http://sources.redhat.com/dm
Source0:    ftp://sources.redhat.com/pub/lvm2/LVM2.2.02.97.tgz
Source100:  device-mapper.yaml
Patch0:     device-mapper-aarch64.patch
Requires:   device-mapper-libs = %{version}-%{release}

%description
This package contains the supporting userspace utility, dmsetup,
for the kernel device-mapper.


%package libs
Summary:    Device-mapper shared library
License:    LGPLv2.1
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Obsoletes:   device-mapper < 1.02.17-6

%description libs
This package contains the device-mapper shared library, libdevmapper.

%package devel
Summary:    Development libraries and headers for device-mapper
License:    LGPLv2.1
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   device-mapper-libs = %{version}-%{release}

%description devel
This package contains files needed to develop applications that use
the device-mapper libraries.



%prep
%setup -q -n LVM2.2.02.97
%patch0 -p1

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --sbindir=/sbin/ \
    --with-user= \
    --with-group= \
    --with-device-uid=0 \
    --with-device-gid=6 \
    --with-device-mode=0660 \
    --enable-pkgconfig


# >> build post
make device-mapper
# << build post

%install
rm -rf %{buildroot}
# >> install pre
make install_device-mapper DESTDIR=$RPM_BUILD_ROOT usrlibdir=$RPM_BUILD_ROOT/usr/%{_lib}
# << install pre

# >> install post
sed -i 's/ (.*)//g' $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc
# << install post


%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc COPYING COPYING.LIB README VERSION_DM WHATS_NEW_DM
/sbin/dmsetup
%doc %{_mandir}/man8/dmsetup.8.gz
# << files

%files libs
%defattr(-,root,root,-)
# >> files libs
%attr(755,root,root) %{_libdir}/libdevmapper.so.*
# << files libs

%files devel
%defattr(-,root,root,-)
# >> files devel
%attr(755,root,root) %{_libdir}/libdevmapper.so
%{_includedir}/libdevmapper.h
%{_libdir}/pkgconfig/*.pc
# << files devel
