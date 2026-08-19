import java.util.*;

class Solution {
    
    // key=곡 제목, value=플레이 타임만큼 기록된 멜로디
    List<Music> info = new ArrayList<>();
    
    public String solution(String m, String[] musicinfos) {
        m = transMelody(m);
        
        for (int i = 0; i < musicinfos.length; i++) {
            String musicInfo = musicinfos[i];
            
            String[] split = musicInfo.split(",");
            String title = split[2];
            String melody = transMelody(split[3]);
            
            int playTime = getPlayTime(split[0], split[1]);
            int melodyLength = melody.length();
            
            String value;
            if (playTime >= melodyLength) {
                int a = playTime/melodyLength;
                int b = playTime%melodyLength;
                value = melody.repeat(a) + melody.substring(0, b);
            } else {
                value = melody.substring(0, playTime);
            }
            info.add(new Music(title, playTime, i, value));
        }
        
        List<Music> cand = new ArrayList<>();
        
        for (Music music : info) {
            if (music.melody.contains(m)) {
                cand.add(music);
            }
        }
        
        List<Music> answer = cand.stream()
            .sorted()
            .toList();
        if (answer.isEmpty()) {
            return "(None)";
        }
        return answer.getFirst().title;
    }
    
    public static int getPlayTime(String start, String end) {
        String[] s1 = start.split(":");
        String[] s2 = end.split(":");
        int h1 = Integer.parseInt(s1[0]);
        int m1 = Integer.parseInt(s1[1]);
        int h2 = Integer.parseInt(s2[0]);
        int m2 = Integer.parseInt(s2[1]);
        
        return (h2*60+m2) - (h1*60+m1);
    }
    
    public String transMelody(String melody) {
        melody = melody.replace("A#", "a");
        melody = melody.replace("G#", "g");
        melody = melody.replace("F#", "f");
        melody = melody.replace("D#", "d");
        melody = melody.replace("C#", "c");
        return melody;
    }
    
    static class Music implements Comparable<Music> {
        String title;
        int playTime;
        int order;
        String melody;
        
        public Music(String title, int playTime, int order, String melody) {
            this.title = title;
            this.playTime = playTime;
            this.order = order;
            this.melody = melody;
        }
        
        @Override
        public int compareTo(Music o) {
            if (playTime == o.playTime) {
                return Integer.compare(order, o.order);
            }
            return -Integer.compare(playTime, o.playTime);
        }
        
        @Override
        public String toString() {
            return "{title=" + title + ", playTime=" + playTime + ", order=" + order + ", melody = " + melody + "}";
        }
    }
}