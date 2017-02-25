%{?_javapackages_macros:%_javapackages_macros}

Summary:	Java client for memcached
Name:		spymemcached
Version:	2.11.4
Release:	1
# ASL src/scripts/write-version-info.sh
License:	ASL 2.0 and MIT
Group:		Development/Java
Url:		https://github.com/dustin/java-memcached-client
Source0:	https://github.com/dustin/java-memcached-client/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(com.codahale.metrics:metrics-core)
BuildRequires:	mvn(junit:junit)
BuildRequires:	mvn(log4j:log4j:1.2.17)
BuildRequires:	mvn(org.jmock:jmock)
BuildRequires:	mvn(org.slf4j:slf4j-api)
BuildRequires:	mvn(org.springframework:spring-beans)

%description
A simple, asynchronous, single-threaded memcached client written in java.

   ·  Efficient storage of objects. General serializable objects are stored
      in their serialized form and optionally compressed if they meet
      criteria. Certain native objects are stored as tightly as possible(for
      example, a Date object generally consumes six bytes, and a Long can be
      anywhere from zero to eight bytes).
   ·  Resilient to server and network outages. In many cases, a client
      operation can be replayed against a server if it goes away and comes
      back. In cases where it can't, it will communicate that as well. An
      exponential backoff reconnect algorithm is applied when a memcached
      becomes unavailable, but asynchronous operations will queue up for the
      server to be applied when it comes back online.
   ·  Operations are asynchronous. It is possible to issue a store and
      continue processing without having to wait for that operation to finish.
      It is even possible to issue a get, do some further processing, check
      the result of the get and cancel it if it doesn't return fast enough.
   ·  There is only one thread for all processing. Regardless of the number of
      requests, threads using the client, or servers to which the client is
      connected, only one thread will ever be allocated to a given
      MemcachedClient.
   ·  Aggressively optimized. There are many optimizations that combine to
      provide high throughput.

%files -f .mfiles
%doc README.markdown
%doc LICENSE.txt

#----------------------------------------------------------------------------

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%files javadoc -f .mfiles-javadoc

#----------------------------------------------------------------------------

%prep
%setup -q -n java-memcached-client-%{version}
# Delete all pre-build binaries
find -name '*.jar' -delete
find -name '*.class' -delete

# fix versions
%pom_xpath_replace "pom:project/pom:version" "
	<version>%{version}</version>"

# fix log4j version
%pom_change_dep log4j:log4j log4j:log4j:1.2.17

# Require an unpachaged version
#pom_remove_dep :jmock
%pom_change_dep jmock org.jmock

%mvn_alias :%{name} spy:spymemcached spy:memcached

%mvn_file :%{name} %{name}-%{version} %{name}

%build

%mvn_build -f -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%changelog
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 gil cattaneo <puntogil@libero.it> - 2.11.4-4
- rebuilt

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.11.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 13 2015 gil cattaneo <puntogil@libero.it> 2.11.4-2
- fix Url tag

* Tue Feb 17 2015 gil cattaneo <puntogil@libero.it> 2.11.4-1
- update to 2.11.4

* Thu Feb 12 2015 gil cattaneo <puntogil@libero.it> 2.9.1-4
- introduce license macro

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.9.1-2
- Use Requires: java-headless rebuild (#1067528)

* Fri Oct 04 2013 gil cattaneo <puntogil@libero.it> 2.9.1-1
- update to 2.9.1

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 gil cattaneo <puntogil@libero.it> 2.9.0-2
- fix mvn aliases

* Thu Jun 13 2013 gil cattaneo <puntogil@libero.it> 2.9.0-1
- update to 2.9.0

* Sun May 12 2013 gil cattaneo <puntogil@libero.it> 2.8.12-1
- update to 2.8.12

* Thu Dec 27 2012 gil cattaneo <puntogil@libero.it> 2.8.9-1
- update to 2.8.9

* Fri Nov 16 2012 gil cattaneo <puntogil@libero.it> 2.8.8-1
- initial rpm
