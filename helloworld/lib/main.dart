import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Drawer + Search Example',
      home: const HomePage(),
    );
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  bool _isSearching = false;
  final TextEditingController _searchController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      // Drawer
      drawer: Drawer(
        child: Builder(
          builder: (context) {
            return Column(
              children: [
                // Top container with back arrow
                Container(
                  color: Colors.teal,
                  width: double.infinity,
                  padding: const EdgeInsets.only(
                      top: 40, left: 16, right: 16, bottom: 16),
                  child: Row(
                    children: [
                      IconButton(
                        icon: const Icon(Icons.arrow_back, color: Colors.white),
                        onPressed: () {
                          Navigator.of(context).pop();
                        },
                      ),
                      const SizedBox(width: 8),
                      const Text(
                        "Menu",
                        style: TextStyle(color: Colors.white, fontSize: 24),
                      ),
                    ],
                  ),
                ),
                ListTile(
                  leading: const Icon(Icons.home),
                  title: const Text("Home"),
                  onTap: () => Navigator.pop(context),
                ),
                ListTile(
                  leading: const Icon(Icons.settings),
                  title: const Text("Settings"),
                  onTap: () {
                    Navigator.pop(context);
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => const SettingsPage()),
                    );
                  },
                ),
              ],
            );
          },
        ),
      ),

      appBar: AppBar(
        backgroundColor: Colors.deepOrange,
        centerTitle: true,
        elevation: 5,
        leading: Builder(
          builder: (context) {
            return IconButton(
              icon: const Icon(Icons.menu),
              onPressed: () {
                Scaffold.of(context).openDrawer();
              },
            );
          },
        ),
        // ✅ Dynamic title or search bar
        title: !_isSearching
            ? const Text("Custom AppBar")
            : TextField(
                controller: _searchController,
                autofocus: true,
                decoration: const InputDecoration(
                  hintText: "Search...",
                  border: InputBorder.none,
                  hintStyle: TextStyle(color: Colors.white54),
                ),
                style: const TextStyle(color: Colors.white, fontSize: 18),
                onSubmitted: (value) {
                  print("Searching for: $value");
                },
              ),
        actions: [
          // 🔍 Search icon
          IconButton(
            icon: Icon(_isSearching ? Icons.close : Icons.search),
            onPressed: () {
              setState(() {
                _isSearching = !_isSearching;
                if (!_isSearching) {
                  _searchController.clear();
                }
              });
            },
          ),

          // ⋮ Overflow menu
          PopupMenuButton<String>(
            onSelected: (value) {
              print("$value clicked");
            },
            itemBuilder: (BuildContext context) {
              return {'Settings', 'About', 'Help'}.map((String choice) {
                return PopupMenuItem<String>(
                  value: choice,
                  child: Text(choice),
                );
              }).toList();
            },
          ),
        ],
      ),

      body: const Center(
        child: Text(
          'Hello, Flutter!\nClick search icon to show search bar.',
          textAlign: TextAlign.center,
        ),
      ),
    );
  }
}

class SettingsPage extends StatelessWidget {
  const SettingsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Settings"),
        backgroundColor: Colors.teal,
      ),
      body: const Center(
        child: Text("This is the Settings Page"),
      ),
    );
  }
}
