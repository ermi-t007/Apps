import React from 'react';
import { Text, View, Button } from 'react-native';

export default function App() {
  return (
    <View style={{flex:1, alignItems:'center', justifyContent:'center'}}>
      <Text style={{fontSize:18, marginBottom:12}}>YouTube Clipper (Expo)</Text>
      <Button title="Open Channel Manager" onPress={() => { /* navigate */ }} />
    </View>
  );
}
