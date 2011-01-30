%define upstream_name	 Class-Autouse
%define upstream_version 2.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Run-time class loading on first method call in Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
Buildrequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Class::Autouse allows you to specify a class that will only load when a method
of that class is called. For large classes that might not be used during the
running of a program, such as Date::Manip, this can save you large amounts of
memory, and decrease the script load time.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
find lib -name \*.pm | xargs chmod 644
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class
%{_mandir}/*/*
