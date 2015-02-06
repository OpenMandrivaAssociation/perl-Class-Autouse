%define upstream_name	 Class-Autouse
%define upstream_version 2.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 2.01
Release:	3

Summary:	Run-time class loading on first method call in Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Class/Class-Autouse-2.01.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Class::Autouse allows you to specify a class that will only load when a method
of that class is called. For large classes that might not be used during the
running of a program, such as Date::Manip, this can save you large amounts of
memory, and decrease the script load time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
find lib -name \*.pm | xargs chmod 644
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*


%changelog
* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.0-1mdv2011.0
+ Revision: 634210
- update to new version 2.00

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.290.0-1mdv2011.0
+ Revision: 406872
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.29-3mdv2009.0
+ Revision: 255887
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Nov 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.29-1mdv2008.1
+ Revision: 110280
- update to new version 1.29

* Fri Jul 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.28-1mdv2008.0
+ Revision: 56128
- update to new version 1.28


* Sat Nov 18 2006 Olivier Thauvin <nanardon@mandriva.org> 1.27-1mdv2007.0
+ Revision: 85430
- 1.27
- Import perl-Class-Autouse

* Sun Apr 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-1mdk
- New release 1.26
- spec cleanup
- fix directory ownership
- better source URL

* Tue Apr 11 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.25-1mdk
- New release 1.25

* Tue Jan 17 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.24-1mdk
- 1.24
- Fix perms

* Tue Oct 04 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.21-1mdk
- New release 1.21

* Sat Aug 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.20-1mdk
- 1.20

* Tue Mar 15 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.17-1mdk
- Initial MDK release.


